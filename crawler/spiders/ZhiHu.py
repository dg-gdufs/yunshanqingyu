"""
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-02-20 18:55:28
LastEditors: Renhetian
LastEditTime: 2022-02-21 19:28:37
"""

import time
import scrapy
from bs4 import BeautifulSoup
from crawler.items import ZhihuItem
from crawler.spiders import BaseSpider
import json


# author:陈宣齐 2022.1.22
class ZhihuSpider(BaseSpider):
    name = 'Zhihu'
    zhihu_id = 0
    topic_id = 0

    def start_requests(self):
        yield scrapy.Request(url='https://www.zhihu.com/topic/{}/index'.format(str(self.topic_id)))

    def parse(self, response, **kwargs):
        soup = BeautifulSoup(response.text, 'lxml')
        for i in soup.select('div.TopicIndex-contentMain > div div.TopicIndexModule-item'):
            meta = {
                'question_id': i.find('a').get('href').split('/')[-1]
            }
            yield scrapy.Request(url='https://www.zhihu.com' + i.find('a').get('href'), callback=self.parse_2,
                                 meta=meta)

    # 处理二级目录，获得关注人数以及浏览者数量
    def parse_2(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        if soup.find('strong', class_='NumberBoard-itemValue') is not None:
            meta = {
                'fellow': soup.find_all('strong', class_='NumberBoard-itemValue')[0].get('title'),
                'browser': soup.find_all('strong', class_='NumberBoard-itemValue')[1].get('title'),
                'question_id': response.meta['question_id']
            }
            data_url = 'https://www.zhihu.com/api/v4/questions/{}/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cvip_info%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=0&platform=desktop&sort_by=default'.format(
                response.meta['question_id'])
            yield scrapy.Request(url=data_url, callback=self.parse_3, meta=meta)

    # 获得回答的json数据，选择字段进行爬取
    def parse_3(self, response):
        item = ZhihuItem()
        data = json.loads(response.text)
        for i in data['data']:
            if i['author']['id'] != '0':
                item['user_id'] = i['author']['id']
            else:
                item['user_id'] = '匿名用户'
            item['answer_id'] = i['id']
            item['like_count'] = i['voteup_count']
            item['reply_count'] = i['comment_count']
            item['question_id'] = i['question']['id']
            item['fellow'] = str(response.meta['fellow'])
            item['browser'] = str(response.meta['browser'])
            data_soup = BeautifulSoup(i['content'], 'lxml')
            item['content'] = ''
            for a in data_soup.select('p'):
                item['content'] += a.text
            item['content'].strip("</p>")
            item['resource'] = []
            for a in data_soup.select('img.origin_image.zh-lightbox-thumb.lazy'):
                item['resource'].append(a.get('data-actualsrc'))
            item['pub_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['updated_time']))
            # 1为是回答，0为回答的评论
            item['is_answer'] = 1
            yield item
            # 如果还有评论就继续爬取
            if i['comment_count'] != '0':
                comments_url = 'https://www.zhihu.com/api/v4/answers/{}/root_comments?limit=10&offset=0&order=normal&status=open'.format(
                    i['id'])
                meta = {
                    'fellow': response.meta['fellow'],
                    'browser': response.meta['browser'],
                    'question_id': i['question']['id']
                }
                yield scrapy.Request(url=comments_url, callback=self.parse_4, meta=meta)
        # 如果不是最后一页，继续翻页
        if data['paging']['is_end'] == 'false':
            meta = {
                'fellow': response.meta['fellow'],
                'browser': response.meta['browser']
            }
            yield scrapy.Request(url=data['paging']['next'], callback=self.parse_3, meta=meta)

    # 爬取回答中的评论
    def parse_4(self, response):
        item = ZhihuItem()
        comments_data = json.loads(response.text)
        for i in comments_data['data']:
            item['content'] = i['content'].strip("</p>")
            item['answer_id'] = i['id']
            item['pub_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['created_time']))
            if i['author']['member']['id'] == '0':
                item['user_id'] = '匿名用户'
            else:
                item['user_id'] = i['author']['member']['id']
            item['like_count'] = i['vote_count']
            item['reply_count'] = i['child_comment_count']
            item['fellow'] = response.meta['fellow']
            item['browser'] = str(response.meta['browser'])
            item['question_id'] = response.meta['question_id']
            item['resource'] = []
            # 1为是回答，0为回答的评论
            item['is_answer'] = 0
            yield item
            if i['child_comment_count'] != '0':
                child_comments_url = 'https://www.zhihu.com/api/v4/comments/{}/child_comments'.format(i['id'])
                meta = {
                    'fellow': response.meta['fellow'],
                    'browser': response.meta['browser'],
                    'question_id': response.meta['question_id']
                }
                yield scrapy.Request(url=child_comments_url, callback=self.parse_5, meta=meta)
        # 如果不是最后一页，继续翻页
        if comments_data['paging']['is_end'] == 'false':
            meta = {
                'fellow': response.meta['fellow'],
                'browser': response.meta['browser'],
                'question_id': response.meta['question_id']
            }
            yield scrapy.Request(url=comments_data['paging']['next'], callback=self.parse_4, meta=meta)

    # 爬取评论的评论
    def parse_5(self, response):
        item = ZhihuItem()
        child_comments_data = json.loads(response.text)
        for i in child_comments_data['data']:
            item['content'] = i['content'].strip("</p>")
            item['answer_id'] = i['id']
            item['like_count'] = i['vote_count']
            item['pub_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['created_time']))
            if i['author']['member']['id'] == '0':
                item['user_id'] = '匿名用户'
            else:
                item['user_id'] = i['author']['member']['id']
            item['reply_count'] = 0
            # 1为是回答，0为回答的评论
            item['is_answer'] = 0
            item['fellow'] = response.meta['fellow']
            item['browser'] = response.meta['browser']
            item['question_id'] = response.meta['question_id']
            item['resource'] = []
            yield item
        # 如果还有下一页
        if child_comments_data['paging']['is_end'] == 'false':
            meta = {
                'fellow': response.meta['fellow'],
                'browser': response.meta['browser'],
                'question_id': response.meta['question_id']
            }
            yield scrapy.Request(url=child_comments_data['paging']['next'], callback=self.parse_5, meta=meta)

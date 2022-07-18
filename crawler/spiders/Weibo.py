from time import time

from bs4 import BeautifulSoup
from crawler.spiders import BaseSpider
from crawler.items import *
from scrapy.http.request import Request

import json
import time


class WeiboSpider(BaseSpider):
    name = 'weibo'
    containerid = ''
    weibo_id = 0
    # 每次爬取前三天数据
    days_ago = 3
    url = 'https://m.weibo.cn/api/container/getIndex?containerid={}&since_id={}'
    url2 = 'https://m.weibo.cn/comments/hotflow?id={}&mid={}'

    def start_requests(self):
        yield Request(self.url.format(self.containerid, ''))

    def parse(self, response):
        item = WeiboItem()
        data = json.loads(response.text)
        last_time = ""
        for i in data['data']['cards']:
            if 'card_group' in i:
                for a in i['card_group']:
                    if 'mblog' in a:
                        # 获得text内容
                        soup = BeautifulSoup(a['mblog']['text'], 'lxml')
                        item['text'] = soup.text
                        item['resource'] = []
                        if soup.find('img') is not None:
                            for img in soup.select('img'):
                                item['resource'].append(img.get('src'))
                        item['user_id'] = str(a['mblog']['user']['id'])
                        item['blog_id'] = a['mblog']['id']
                        item['user_image'] = a['mblog']['user']['profile_image_url']
                        item['parent_blog_id'] = None
                        item['like_count'] = a['mblog']['attitudes_count']
                        item['reply_count'] = a['mblog']['comments_count']
                        item['pub_time'] = form_time(a['mblog']['created_at'])
                        last_time = item['pub_time']
                        item['reposts_count'] = a['mblog']['reposts_count']
                        item['is_origin'] = 1
                        item['user_name'] = a['mblog']['user']['screen_name']
                        yield item
                        # 当评论不为0是，爬取评论信息
                        if a['mblog']['comments_count'] > 0:
                            comments_url = self.url2.format(a['mblog']['id'], a['mblog']['mid'])
                            meta = {'blog_id': a['mblog']['id'], }
                            yield scrapy.Request(url=comments_url, callback=self.parse_2, meta=meta)
        # 爬取下一页
        if data.get('data', {}).get('pageInfo', {}).get('since_id'):
            # TODO: 时间截止
            if self.weibo_time_judge(last_time):
                since_id = str(data['data']['pageInfo']['since_id'])
                yield scrapy.Request(self.url.format(self.containerid, since_id), callback=self.parse)
            else:
                self.send_log(1, "<--------------------------------------------超过时间，不进行翻页"
                                 "-------------------------------------------->")
                self.send_log(1, "<--------------------------------------------超过时间，不进行翻页"
                                 "-------------------------------------------->")
                self.send_log(1, "<--------------------------------------------超过时间，不进行翻页"
                                 "-------------------------------------------->")
                self.send_log(1, "<--------------------------------------------超过时间，不进行翻页"
                                 "-------------------------------------------->")
                self.send_log(1, "<--------------------------------------------超过时间，不进行翻页"
                                 "-------------------------------------------->")

    def parse_2(self, response):
        item = WeiboItem()
        comments_data = json.loads(response.text)
        if 'data' in comments_data:
            for comment in comments_data['data']['data']:
                item['user_id'] = str(comment['user']['id'])
                item['user_name'] = comment['user']['screen_name']
                item['user_image'] = comment['user']['profile_image_url']
                comments_soup = BeautifulSoup(comment['text'], 'lxml')
                item['text'] = comments_soup.text
                item['is_origin'] = 0
                item['resource'] = []
                if comments_soup.find('img') is not None:
                    for comments_img in comments_soup.select('img'):
                        item['resource'].append(comments_img.get('src'))
                item['pub_time'] = form_time(comment['created_at'])
                item['like_count'] = comment['like_count']
                item['reposts_count'] = 0
                item['reply_count'] = comment['total_number']
                item['parent_blog_id'] = response.meta['blog_id']
                item['blog_id'] = comment['id']
                yield item
                # 爬取回复的回复
                if 'comments' in comment and comment['comments']:
                    for comments_comment in comment['comments']:
                        comments_item = WeiboItem()
                        comments_comment_soup = BeautifulSoup(comments_comment['text'], 'lxml')
                        comments_item['text'] = comments_comment_soup.text
                        comments_item['pub_time'] = form_time(comments_comment['created_at'])
                        comments_item['user_id'] = str(comments_comment['user']['id'])
                        comments_item['user_name'] = comments_comment['user']['screen_name']
                        comments_item['user_image'] = comments_comment['user']['profile_image_url']
                        comments_item['parent_blog_id'] = comment['id']
                        comments_item['blog_id'] = comments_comment['id']
                        comments_item['is_origin'] = 0
                        comments_item['resource'] = []
                        comments_item['like_count'] = 0
                        comments_item['reposts_count'] = 0
                        comments_item['reply_count'] = 0
                        yield comments_item

    def weibo_time_judge(self, time_str):
        # 2021-01-01 00:00:00 1609434000
        if int(time.mktime(time.strptime(time_str, "%Y-%m-%d %H:%M:%S"))) > int(time.time()) - int(
                self.days_ago) * 86400:
            return True
        return False


def form_time(wb_time):
    # Sun Mar 13 22:26:11 +0800 2022
    # 2022-03-01 17:28:00
    result = ''
    times = wb_time.split(' ')
    result += times[5] + '-'
    if times[1] == 'Jan':
        result += '01-'
    elif times[1] == 'Feb':
        result += '02-'
    elif times[1] == 'Mar':
        result += '03-'
    elif times[1] == 'Apr':
        result += '04-'
    elif times[1] == 'May':
        result += '05-'
    elif times[1] == 'Jun':
        result += '06-'
    elif times[1] == 'Jul':
        result += '07-'
    elif times[1] == 'Aug':
        result += '08-'
    elif times[1] == 'Sep':
        result += '09-'
    elif times[1] == 'Oct':
        result += '10-'
    elif times[1] == 'Nov':
        result += '11-'
    else:
        result += '12-'
    result += times[2] + ' ' + times[3]
    return result

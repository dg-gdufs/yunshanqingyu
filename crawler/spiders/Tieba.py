'''
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-01-26 15:39:36
LastEditors: Renhetian
LastEditTime: 2022-03-02 14:02:36
'''

from config.host_config import IPIDEA_API
from time import time
from crawler.spiders import BaseSpider
from crawler.items import *
from utils.date_util import DateUtil
from scrapy.http.request import Request
import requests

from lxml import etree
import re
import json
import time
from datetime import datetime


class TiebaSpider(BaseSpider):
    name = 'tieba'
    kw = ''
    qw = open('config/qw_words.txt', 'r', encoding='utf-8').read().splitlines()
    tieba_id = 0
    days_ago = 1
    start_page = 0
    now_proxy = ""
    last_clean_ip_time = 0

    url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
    search_url = 'https://tieba.baidu.com/f/search/res?ie=utf-8&isnew=1&kw={}&qw={}&un=&rn=10&pn=1&sd=&ed=&sm=1&only_thread=1'
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {'Cookie': open('config/tieba_cookie.txt', 'r', encoding='utf-8').read()}
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
        'Cookie': open('config/tieba_cookie.txt', 'r', encoding='utf-8').read()
    }

    def start_requests(self):
        start_pn = int(self.start_page) * 50
        yield Request(IPIDEA_API, callback=self.parse_proxy)
        yield Request(self.url.format(self.kw, start_pn), meta={'pn': start_pn})
        if self.qw:
            for i in self.qw:
                yield Request(self.search_url.format(self.kw, i), meta={'qw': i})

    def parse(self, response):
        if int(time.time()) - self.last_clean_ip_time > 60:
            yield Request(IPIDEA_API, callback=self.parse_proxy)

        if response.url.startswith('https://wappass.baidu.com'):
            self.send_log(3, "网页被风控 ==> url:<{}>".format(response.url))
            return
        # 判断是否为搜索的url
        if response.url.startswith('https://tieba.baidu.com/f/search/res?'):
            self.send_log(1, "<----------------------正在爬取贴吧搜索，搜索关键词为 < {} >"
                             "---------------------->".format(response.meta['qw']))
            html = etree.HTML(response.text)
            for i in html.xpath('//div[@class="s_post"]/span[@class="p_title"]'):
                main_post_id = re.findall(r'\d+', i.xpath('a/@href')[0])[0]
                yield Request('https://tieba.baidu.com/p/' + main_post_id,
                              meta={'is_origin': 1, 'main_post_id': main_post_id}, callback=self.parse_item)
            timestamp = int(time.mktime(time.strptime(html.xpath('//font[@class="p_green p_date"]')[-1].xpath('text()')[0], "%Y-%m-%d %H:%M")))
            if html.xpath('//a[@class="next"]/@href') and timestamp > 1609430400:
                self.send_log(1, "贴吧关键词搜索翻页成功，下一页 ===> url:<{}>".format(
                    'https://tieba.baidu.com' + html.xpath('//a[@class="next"]/@href')[0]))
                yield Request('https://tieba.baidu.com' + html.xpath('//a[@class="next"]/@href')[0], meta=response.meta,
                              callback=self.parse)
        else:
            html = etree.HTML(response.text.replace('<!--', '<div>').replace('-->', '</div>'))
            for data in html.xpath('//ul[@id="thread_list"]/li[@data-field]/@data-field'):
                main_post_id = str(json.loads(data)['id'])
                yield Request('https://tieba.baidu.com/p/' + main_post_id, meta={'is_origin': 1, 'main_post_id': main_post_id}, callback=self.parse_item)
            # 时间判断
            time_str = re.findall(r'创建时间.+?</span>', response.text)[-1].strip('创建时间">').strip("</span>")
            if time_str and self.tieba_time_judge(time_str):
                response.meta['pn'] += 50
                self.send_log(1, "翻页成功，下一页 ===> url:<{}>".format(self.url.format(self.kw, response.meta['pn'])))
                yield Request(self.url.format(self.kw, response.meta['pn']), meta=response.meta)
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

    def parse_item(self, response):
        if response.url.startswith('https://wappass.baidu.com'):
            self.send_log(3, "网页被风控 ==> url:<{}>".format(response.url))
            return
        html = etree.HTML(response.text.replace('<!--', '<div>').replace('-->', '</div>'))

        item_list = html.xpath('//div[@class="p_postlist"]/div[@data-field]')
        # 爬取主贴
        if response.meta['is_origin'] == 1:
            origin = item_list[0]
            del item_list[0]
            js = json.loads(origin.xpath('./@data-field')[0])
            item = TiebaItem()
            item['post_id'] = str(js['content']['post_id'])
            item['main_post_id'] = response.meta['main_post_id']
            item['tieba_id'] = self.tieba_id
            item['user_id'] = js['author']['user_id']
            try:
                item['level'] = js['author']['level_id']
            except:
                item['level'] = '0'
            item['user_home'] = js['author']['portrait']
            item['is_origin'] = 1
            text = origin.xpath('.//div[starts-with(@id, "post_content_")]//text()')
            item['content'] = '\n'.join(text).strip()
            item['resource'] = []
            for i in origin.xpath('.//div[starts-with(@id, "post_content_")]//img/@src'):
                item['resource'].append(i)
            item['reply_count'] = js['content']['comment_num']
            item['pub_time'] = js['content']['date']
            item['user_name'] = js['author']['user_name'].strip('"user_name":').strip('"')
            yield item
            response.meta['is_origin'] = 0
            # 爬取标题
            item = TiebaItem()
            item['tieba_id'] = self.tieba_id
            item['main_post_id'] = response.meta['main_post_id']
            item['post_id'] = response.meta['main_post_id']
            item['content'] = re.findall(r'title=".*"', re.findall(r'core_title_txt.+?title=".+?"',
                                                                   response.text)[0])[0].strip('title=').strip('"')
            item['pub_time'] = js['content']['date']
            item['is_origin'] = 0
            item['resource'] = []
            item['user_id'] = js['author']['user_id']
            yield item

        # 爬取帖子
        for i in item_list:
            js = json.loads(i.xpath('./@data-field')[0])
            item = TiebaItem()
            item['post_id'] = js['content']['post_id']
            item['main_post_id'] = response.meta['main_post_id']
            item['tieba_id'] = self.tieba_id
            item['user_id'] = js['author']['user_id']
            try:
                item['level'] = js['author']['level_id']
            except:
                item['level'] = '0'
            item['user_home'] = js['author']['portrait']
            item['is_origin'] = 0
            text = i.xpath('.//div[starts-with(@id, "post_content_")]//text()')
            item['content'] = '\n'.join(text).strip()
            item['resource'] = []
            for i in i.xpath('.//div[starts-with(@id, "post_content_")]//img/@src'):
                item['resource'].append(i)
            item['reply_count'] = js['content']['comment_num']
            item['pub_time'] = js['content']['date']
            item['user_name'] = js['author']['user_name'].strip('"user_name":').strip('"')
            yield item
        # 爬取帖子回复
        reply_list = re.findall(r'"\d*":\[\{"comment_id":.+?\}\]', response.text)
        userList = json.loads(re.findall(r'"userList" :.+?"commentList"', response.text)
                              [0].strip(',    "commentList"').strip('userList" : '))
        for i in reply_list:
            item = TiebaItem()
            item['pid'] = re.findall(r'\d+', i)[0]
            i = re.findall(r'\{"comment_id":.+?\}', i)[0]
            js = json.loads(i)
            item['post_id'] = str(js['comment_id'])
            item['main_post_id'] = response.meta['main_post_id']
            item['tieba_id'] = self.tieba_id
            item['user_id'] = str(js['user_id'])
            if userList[str(js['user_id'])]['user_name']:
                item['user_name'] = userList[str(js['user_id'])]['user_name']
            elif userList[str(js['user_id'])]['user_nickname']:
                item['user_name'] = userList[str(js['user_id'])]['user_nickname']
            else:
                item['user_name'] = userList[str(js['user_id'])]['show_nickname']
            item['user_home'] = userList[str(js['user_id'])]['portrait']
            item['is_origin'] = 0
            item['content'], item['resource'] = self.content_format(js['content'])
            item['pub_time'] = DateUtil.time_stamp2formate_time(js['now_time'])
            try:
                if userList[str(js['user_id'])]['mParr_props']:
                    item['level'] = userList[str(js['user_id'])]['mParr_props']['all_level']['2']['level']
            except:
                item['level'] = 0
            yield item

        next_url = html.xpath('//ul[@class="l_posts_num"]//a[contains(text(), "下一页")]/@href')
        if next_url:
            yield Request('https://tieba.baidu.com' + next_url[0], meta=response.meta, callback=self.parse_item)

    def parse_proxy(self, response):
        self.last_clean_ip_time = int(time.time())
        ipList = response.text
        pro = 'https://{}'.format(ipList.split('\r\n')[0])
        self.send_log(1, "proxy已更新 ==> {}".format(pro))
        self.now_proxy = pro

    def content_format(self, content):
        out1 = re.subn(r'<img.*?>', '', content)[0]
        out1 = re.subn(r'<a.*?>', '', out1)[0]
        out1 = re.subn(r'</a.*?>', '', out1)[0]
        out1 = out1.strip()
        out2 = re.findall(r'<img.*?src="(.*?)".*?>', content)
        return out1, out2

    def tieba_time_judge(self, time_str):
        if ':' in time_str:
            return True
        # 同一年显示年份6-26
        if len(time_str.split('-')[0]) < 4:
            year = datetime.now().date().strftime("%Y")
            timestamp = int(time.mktime(time.strptime(year + '-' + time_str, "%Y-%m-%d")))
        else:
            # 2018-6
            timestamp = int(time.mktime(time.strptime(time_str + '-01', "%Y-%m-%d")))
        # if timestamp > int(time.time()) - int(self.days_ago)*86400:
        # 1609430400
        if timestamp > int(time.time()) - int(self.days_ago) * 86400:
            return True
        return False

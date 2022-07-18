'''
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-03-01 22:56:12
LastEditors: Renhetian
LastEditTime: 2022-03-02 00:59:25
'''
# encoding: utf-8

import random
from scrapy.exceptions import IgnoreRequest

from common.header import *
from common.sql import *
from crawler.items import *
from utils.format_util import FormatUtil

class FilterSpiderMiddleware:
    '''
    过滤器下载中间件
    '''
    def process_spider_output(self, response, result, spider):
        try:
            for i in result:
                if isinstance(i, TiebaItem):
                    sql = TIEBA_SQL_FILTER.format(i['post_id'])
                    result_ = spider.news_db.select(sql)
                    if result_:
                        spider.send_log(1, "贴吧帖子{}已存在".format(i['post_id']))
                        continue

                elif isinstance(i, WeiboItem):
                    sql = WEIBO_SQL_FILTER.format(i['blog_id'])
                    result_ = spider.news_db.select(sql)
                    if result_:
                        spider.send_log(1, "微博超话帖子{}已存在".format(i['blog_id']))
                        continue

                yield i
        except Exception as e:
            spider.send_log(3, "FilterSpiderMiddleware error ==> {}".format(e))


            
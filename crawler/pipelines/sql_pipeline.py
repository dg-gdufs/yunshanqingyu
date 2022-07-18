'''
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-01-26 14:28:19
LastEditors: Renhetian
LastEditTime: 2022-03-01 23:18:32
'''
# encoding: utf-8

import json
from utils.date_util import DateUtil
from utils.format_util import FormatUtil
from common.db_keys import *
from crawler.items import *

class SqlPipeline:
    '''
    录入SQL的Pipeline
    '''

    def process_item(self, item, spider):
        try:
            # 丢弃ack
            if isinstance(item, AckItem):
                return item

            if isinstance(item, TiebaItem):
                # resource优化
                if 'resource' not in item:
                    item['resource'] = []
                item['resource'] = json.dumps(item['resource'])
                # cole_time生成
                item['cole_time'] = DateUtil.time_now_formate()
                # 数据库insert
                keylist = []
                valuelist = []
                for i in TIEBA_KEYS:
                        if i not in item:
                                continue
                        keylist.append(i)
                        valuelist.append(item[i])
                spider.news_db.insert('tieba', keylist, valuelist)
                if item['is_origin'] == 1:
                    spider.send_log(1, "贴吧主贴获取成功 ==> main_post_id:<{}>".format(item['main_post_id']))
                else:
                    spider.send_log(1, "回复获取成功 ==> post_id:<{}>".format(item['post_id']))
                return item

            if isinstance(item, WeiboItem):
                # resource优化
                if 'resource' not in item:
                    item['resource'] = []
                item['resource'] = json.dumps(item['resource'])
                # cole_time生成
                item['cole_time'] = DateUtil.time_now_formate()
                item['weibo_id'] = spider.weibo_id
                # 数据库insert
                keylist = []
                valuelist = []
                for i in WEIBO_KEYS:
                        if i not in item:
                                continue
                        keylist.append(i)
                        valuelist.append(item[i])
                spider.news_db.insert('weibo', keylist, valuelist)
                if item['is_origin'] == 1:
                    spider.send_log(1, "微博主贴获取成功 ==> parent_blog_id:<{}>".format(item['blog_id']))
                else:
                    spider.send_log(1, "回复获取成功 ==> blog_id:<{}>".format(item['blog_id']))
                return item
            
            return item
        except Exception as e:
            spider.send_log(3, "SqlPipeline error ==> {} ==> item:{}".format(e, item))
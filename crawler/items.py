'''
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-01-26 14:28:19
LastEditors: Renhetian
LastEditTime: 2022-03-02 00:30:02
'''

import scrapy
from scrapy import Field


class AckItem(scrapy.Item):
    res = Field()


class TiebaItem(scrapy.Item):
    post_id = Field(serializer=str)  # 此回复的id
    main_post_id = Field(serializer=str)  # 此回复对应帖子的id
    tieba_id = Field(serializer=int)  # 贴吧的id
    user_id = Field(serializer=str)  # 回复用户id
    level = Field(serializer=int)  # 回复用户贴吧等级
    is_origin = Field(serializer=bool)  # 是否是主贴
    content = Field(serializer=str)  # 内容
    resource = Field(serializer=str)  # 多媒体文件
    # like_count = Field(serializer=int)
    reply_count = Field(serializer=int)  # 回复数
    pub_time = Field(serializer=str)  # 发布时间
    cole_time = Field(serializer=str)  # 爬取时间
    user_home = Field(serializer=str)  # 用户主页
    pid = Field(serializer=str)  # 回复所属从贴
    user_name = Field(serializer=str)  # 用户名


class ZhihuItem(scrapy.Item):
    question_id = Field()
    answer_id = Field()
    user_id = Field()
    school_id = Field()
    content = Field()
    resource = Field()
    is_answer = Field()
    like_count = Field()
    reply_count = Field()
    fellow = Field()
    browser = Field()
    pub_time = Field()
    cole_time = Field()


class WeiboItem(scrapy.Item):
    blog_id = Field()
    weibo_id = Field()
    parent_blog_id = Field()
    user_id = Field()
    user_name = Field()
    text = Field()
    like_count = Field()
    reply_count = Field()
    reposts_count = Field()
    is_origin = Field()
    resource = Field()
    pub_time = Field()
    cole_time = Field()
    user_image = Field()

'''
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-01-26 14:28:19
LastEditors: Renhetian
LastEditTime: 2022-02-14 13:05:18
'''
# encoding: utf-8

class ReplyDownloaderMiddleware:
    '''
    reply下载中间件
    '''

    def process_response(self, request, response, spider):
        try:
            if response.status >= 300 or response.status <200:
                spider.send_log(2, "状态码错误 ==> status:{} ==> url:<{}>".format(response.status, response.url))
            else:
                spider.send_log(1, "状态码正常 ==> status:{} ==> url:<{}>".format(response.status, response.url))
            if response.url.startswith('https://wappass.baidu.com'):
                spider.send_log(3, "网页被风控 ==> url:<{}>".format(response.url))
            else:
                return response
        except Exception as e:
            spider.send_log(3, "ReplyDownloaderMiddleware error ==> {} ==> url:<{}>".format(e, response.url))

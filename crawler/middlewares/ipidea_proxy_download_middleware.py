'''
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-02-14 13:02:08
LastEditors: Renhetian
LastEditTime: 2022-02-14 14:46:47
'''

import requests
import json
import random
from config.host_config import *

class IpideaProxyDownloaderMiddleware:
    '''
    proxy下载中间件
    '''

    proxy_list = []

    def process_request(self, request, spider): 
        try:
            if len(self.proxy_list) < 10:
                self.get_proxy_list(spider)
            request.meta['proxy'] = self.proxy_list[random.randint(0,len(self.proxy_list)-1)]
            spider.send_log(1, "proxy已插入 ==> {}".format(request.meta['proxy']))
            return None
        except Exception as e:
            spider.send_log(3, "IpideaProxyDownloaderMiddleware error ==> {} ==> url:<{}>".format(e, request.url))

    def process_response(self, request, response, spider):
        try:
            if response.status >= 300 or response.status <200 or response.url.startswith('https://wappass.baidu.com'):
                index = self.proxy_list.index(request.meta['proxy'])
                del self.proxy_list[index]
            spider.send_log(1, "proxy异常，删除当前代理 ==> {}".format(request.meta['proxy']))
            return response
        except Exception as e:
            spider.send_log(3, "ReplyDownloaderMiddleware error ==> {} ==> url:<{}>".format(e, response.url))

    def get_proxy_list(self, spider):
        ipList = requests.get(IPIDEA_API).text
        for i in ipList.split('\r\n'):
            self.proxy_list.append('https://{}:{}'.format(i.split(':')[0], str(i.split(':')[1])))
        spider.send_log(1, "proxy列表已更新 ==> num:<{}>".format(len(self.proxy_list)))
'''
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-02-14 13:02:08
LastEditors: Renhetian
LastEditTime: 2022-02-14 14:46:47
'''

import time
import requests
import json
import random
from config.host_config import *

class IpideaProxyDownloaderMiddleware:
    '''
    proxy下载中间件
    '''

    def process_request(self, request, spider): 
        try:
            if request.url.startswith("https://tieba.baidu.com"):
                request.meta['proxy'] = spider.now_proxy
            return None
        except Exception as e:
            spider.send_log(3, "IpideaProxyDownloaderMiddleware error ==> {} ==> url:<{}>".format(e, request.url))

    def process_response(self, request, response, spider):
        try:
            if response.status >= 300 or response.status <200 or response.url.startswith('https://wappass.baidu.com'):
                spider.send_log(1, "proxy异常，删除当前代理 ==> {}".format(request.meta['proxy']))
                self.get_proxy(spider)
            return response
        except Exception as e:
            spider.send_log(3, "ReplyDownloaderMiddleware error ==> {} ==> url:<{}>".format(e, response.url))

    def get_proxy(self, spider):
        spider.last_clean_ip_time = int(time.time())
        ipList = requests.get(IPIDEA_API).text
        pro = 'http://{}'.format(ipList.split('\r\n')[0])
        spider.send_log(1, "proxy已更新 ==> {}".format(pro))
        spider.now_proxy = pro
        
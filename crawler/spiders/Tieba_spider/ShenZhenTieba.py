'''
Description: file description
Version: 1.0
Autor: Renhetian
Date: 2022-01-26 17:07:45
LastEditors: Renhetian
LastEditTime: 2022-02-20 17:10:42
'''

from crawler.spiders.Tieba import TiebaSpider


class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'shenzhentieba'
    kw = '深圳大学'
    tieba_id = 8
from crawler.spiders.Tieba import TiebaSpider

class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'foshankexuejishutieba'
    kw = '佛山科学技术学院'
    tieba_id = 18
from crawler.spiders.Tieba import TiebaSpider

class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'zhaoqingtieba'
    kw = '肇庆学院'
    tieba_id = 22
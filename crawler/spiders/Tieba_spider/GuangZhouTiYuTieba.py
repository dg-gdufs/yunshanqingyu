from crawler.spiders.Tieba import TiebaSpider

class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'guangzhoutiyutieba'
    kw = '广州体育学院'
    tieba_id = 28
from crawler.spiders.Tieba import TiebaSpider

class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'guangdongjinrongtieba'
    kw = '广东金融学院'
    tieba_id = 17
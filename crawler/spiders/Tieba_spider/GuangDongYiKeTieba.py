from crawler.spiders.Tieba import TiebaSpider

class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'guangdongyiketieba'
    kw = '广东医科大学'
    tieba_id = 30
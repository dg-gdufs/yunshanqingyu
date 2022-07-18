from crawler.spiders.Tieba import TiebaSpider

class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'guangzhouyiketieba'
    kw = '广州医科大学'
    tieba_id = 25
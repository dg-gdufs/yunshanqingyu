from crawler.spiders.Tieba import TiebaSpider


class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'guangzhoutieba'
    kw = '广州大学'
    tieba_id = 11
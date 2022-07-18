from crawler.spiders.Tieba import TiebaSpider


class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'dongguanligongtieba'
    kw = '东莞理工学院'
    tieba_id = 13

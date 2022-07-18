from crawler.spiders.Tieba import TiebaSpider

class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'zhongkainongyetieba'
    kw = '仲恺农业工程学院'
    tieba_id = 21
from crawler.spiders.Tieba import TiebaSpider

class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'shaoguantieba'
    kw = '韶关学院'
    tieba_id = 20
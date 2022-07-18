from crawler.spiders.Tieba import TiebaSpider

class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'guangzhoumeishutieba'
    kw = '广州美术学院'
    tieba_id = 26
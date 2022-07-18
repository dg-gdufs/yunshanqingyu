from crawler.spiders.Tieba import TiebaSpider

class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'guangdongjishushifantieba'
    kw = '广东技术师范大学'
    tieba_id = 19
from crawler.spiders.Tieba import TiebaSpider

class GuangwaiTiebaSpider(TiebaSpider):
    #
    name = 'guangdongyaoketieba'
    kw = '广东药科大学'
    tieba_id = 27
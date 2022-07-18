from crawler.spiders.Tieba import TiebaSpider


class GuangwaiTiebaSpider(TiebaSpider):
    name = 'huananligongtieba'
    kw = '华南理工大学'
    tieba_id = 3
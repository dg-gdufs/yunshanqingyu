from crawler.spiders.Tieba import TiebaSpider


class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'shantoutieba'
    kw = '汕头大学'
    tieba_id = 12
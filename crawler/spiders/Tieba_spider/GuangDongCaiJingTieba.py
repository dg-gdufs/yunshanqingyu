from crawler.spiders.Tieba import TiebaSpider


class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'guangdongcaijingtieba'
    kw = '广东财经大学'
    tieba_id = 14
from crawler.spiders.Tieba import TiebaSpider

class GuangwaiTiebaSpider(TiebaSpider):
    # 拿不到data
    name = 'guangdonghaiyangtieba'
    kw = '广东海洋大学'
    tieba_id = 15
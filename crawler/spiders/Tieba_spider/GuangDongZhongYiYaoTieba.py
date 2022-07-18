from crawler.spiders.Tieba import TiebaSpider

class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'guangdongzhongyiyaotieba'
    kw = '广州中医药大学'
    tieba_id = 24
from crawler.spiders.Tieba import TiebaSpider


class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'nanfangyiketieba'
    kw = '南方医科大学'
    tieba_id = 10
from crawler.spiders.Tieba import TiebaSpider


class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'nanfangkejitieba'
    kw = '南方科技大学'
    tieba_id = 9
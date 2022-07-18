from crawler.spiders.Tieba import TiebaSpider


class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'guanggongtieba'
    kw = '广东工业大学'
    tieba_id = 7
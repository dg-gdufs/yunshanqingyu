from crawler.spiders.Tieba import TiebaSpider

class GuangwaiTiebaSpider(TiebaSpider):
    # 拿不到data
    name = 'wuyitieba'
    kw = '五邑大学'
    tieba_id = 16
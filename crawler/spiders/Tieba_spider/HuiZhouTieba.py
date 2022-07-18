from crawler.spiders.Tieba import TiebaSpider

class GuangwaiTiebaSpider(TiebaSpider):
    # 找不到时间
    name = 'huizhoutieba'
    kw = '惠州学院'
    tieba_id = 23
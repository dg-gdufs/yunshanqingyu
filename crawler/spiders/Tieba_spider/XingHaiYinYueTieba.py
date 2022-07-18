from crawler.spiders.Tieba import TiebaSpider

class GuangwaiTiebaSpider(TiebaSpider):
    # 已全爬
    name = 'xinghaiyinyuetieba'
    kw = '星海音乐学院'
    tieba_id = 29
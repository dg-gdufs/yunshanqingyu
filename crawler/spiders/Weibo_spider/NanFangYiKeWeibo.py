from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'nanfangyikeweibo'
    containerid = '1008084f2bf2d3f3cb6ed1686b100c5e25a3fe'
    weibo_id = 10
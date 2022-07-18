from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'shaoguanweibo'
    containerid = '1008086b4c7ef3b926bef19f2c2a52c74853f2'
    weibo_id = 20

from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据,已爬
    name = 'guangwaiweibo'
    containerid = '100808d1581a8658d64a58b5b90b2dfb933e01'
    weibo_id = 1
    
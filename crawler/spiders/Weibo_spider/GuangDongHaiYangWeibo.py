from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'guangdonghaiyangweibo'
    containerid = '100808648570dbd00f0e44afbbe75527731c37'
    weibo_id = 15
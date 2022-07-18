from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'huananligongweibo'
    containerid = '10080857341c8431643bc3d4c69659e557b996'
    weibo_id = 3

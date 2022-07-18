from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'shantouweibo'
    containerid = '10080815f498f582f3b49d471664034551d9f2'
    weibo_id = 12
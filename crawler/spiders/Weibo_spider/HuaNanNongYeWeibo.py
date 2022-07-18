from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'huanannongyeweibo'
    containerid = '1008086eb3a5a6ded91474f3d4b254f6fe9aa0'
    weibo_id = 5
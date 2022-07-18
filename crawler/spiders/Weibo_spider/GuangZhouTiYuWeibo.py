from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'guangzhoutiyuweibo'
    containerid = '1008082a99e005ad4d2080a62fa4c719d4d7e6'
    weibo_id = 28
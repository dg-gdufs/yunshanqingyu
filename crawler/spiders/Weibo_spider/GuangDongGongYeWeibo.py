from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'guangdonggongyeweibo'
    containerid = '1008083206e0937e5dcac54ad4ca6430ee337a'
    weibo_id = 7
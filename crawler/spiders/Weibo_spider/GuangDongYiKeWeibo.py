from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'guangdongyikeweibo'
    containerid = '100808a697849f08e2a68b2bf289a50f37cc8e'
    weibo_id = 30
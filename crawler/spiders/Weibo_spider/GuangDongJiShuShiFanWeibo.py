from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'guangdongjishushifanweibo'
    containerid = '100808a75afe92ccc092a4025c9d08992bd2c9'
    weibo_id = 19
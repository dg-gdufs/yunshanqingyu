from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'guangzhoumeishuweibo'
    containerid = '10080853d0c82a8570aeaf866b5e0b0dba307d'
    weibo_id = 26
from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'huizhouweibo'
    containerid = '1008087ec4260c2b38bfa7807544a15e3e8a46'
    weibo_id = 23
from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'zhongkainongyeweibo'
    containerid = '100808c2f139bb28cff8c3930712d949769953'
    weibo_id = 21
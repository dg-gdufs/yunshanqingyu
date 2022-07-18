from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据已全爬
    name = 'guangzhouweibo'
    containerid = '100808ce66afdff6257581599a44f4768d7d69'
    weibo_id = 11
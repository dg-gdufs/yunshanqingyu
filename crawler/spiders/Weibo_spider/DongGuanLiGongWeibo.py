from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据
    name = 'dongguanligongweibo'
    containerid = '100808b8a48c18d8cf9673e30f70a9607471e6'
    weibo_id = 13
from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'foshankexuejishuweibo'
    containerid = '100808165ef5c505a4b4f59142bc0a0f0aafae'
    weibo_id = 18
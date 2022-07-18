from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'guangdongcaijingweibo'
    containerid = '100808d8313f40312676f65e5e708767cf9a7f'
    weibo_id = 14
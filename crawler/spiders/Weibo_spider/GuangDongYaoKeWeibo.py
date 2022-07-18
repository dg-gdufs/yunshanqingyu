from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'guangdongyaokeweibo'
    containerid = '100808ddcbcbecbb9d78d9bb9ad65e09dfe903'
    weibo_id = 27
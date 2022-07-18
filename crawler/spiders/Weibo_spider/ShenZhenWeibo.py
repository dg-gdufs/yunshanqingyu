from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'shenzhenweibo'
    containerid = '1008082d8094422473dc526f041deb05459ebb'
    weibo_id = 8
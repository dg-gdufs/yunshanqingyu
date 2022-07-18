from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'guangdongzhongyiyaoweibo'
    containerid = '1008089aaeff560f4fd4d61f8ce24eb884092c'
    weibo_id = 24
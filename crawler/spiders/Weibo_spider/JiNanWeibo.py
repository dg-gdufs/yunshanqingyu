from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'jinanweibo'
    containerid = '100808c84358219033ae6f344609b36d22d3aa'
    weibo_id = 4
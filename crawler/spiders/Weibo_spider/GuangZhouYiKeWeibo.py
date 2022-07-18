from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'guangzhouyikeweibo'
    containerid = '100808d07024dc0c46ee2c9c099e302c41a114'
    weibo_id = 25
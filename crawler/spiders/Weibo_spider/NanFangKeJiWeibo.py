from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'nanfangkejiweibo'
    containerid = '100808b6dda14d1411dd96b3f03689a37f4fb2'
    weibo_id = 9
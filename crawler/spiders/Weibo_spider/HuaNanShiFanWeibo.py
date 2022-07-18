from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'huananshifanweibo'
    containerid = '100808230ff7b3d00f23cf23b1dc047d3401ca'
    weibo_id = 6
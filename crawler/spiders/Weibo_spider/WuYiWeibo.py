from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'wuyiweibo'
    containerid = '1008085b52b5900d86efb3520eb833f569959d'
    weibo_id = 16
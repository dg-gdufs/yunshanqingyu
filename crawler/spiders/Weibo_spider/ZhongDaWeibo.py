from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'zhongdaweibo'
    containerid = '1008080949a196008757bc02e335870658cc83'
    weibo_id = 2

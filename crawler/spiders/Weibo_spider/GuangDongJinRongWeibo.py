from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据，已全爬
    name = 'guangdongjinrongweibo'
    containerid = '100808bd97588bcf8558647b2e1ae3b83ab97f'
    weibo_id = 17
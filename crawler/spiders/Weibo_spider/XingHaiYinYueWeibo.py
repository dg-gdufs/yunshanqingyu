from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据
    name = 'xinghaiyinyueweibo'
    containerid = '1008085ee522dd496a22856ff9ddf2c20ba8d8'
    weibo_id = 29
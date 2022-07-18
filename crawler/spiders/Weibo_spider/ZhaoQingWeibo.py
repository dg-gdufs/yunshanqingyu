from crawler.spiders.Weibo import WeiboSpider


class GuangwaiWeiboSpider(WeiboSpider):
    # 需要重写以下数据
    name = 'zhaoqingweibo'
    containerid = '100808f747262a5c189d90e10780d2f7dd4378'
    weibo_id = 22
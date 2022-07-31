# encoding: utf-8

import os
import fire
from apscheduler.schedulers.blocking import BlockingScheduler

def run(db, days_ago):
    command1 = 'scrapy crawl {} -a db={} -a days_ago={} -a start_page=0'
    command2 = 'scrapy crawl {} -a db={}'
    try:
        with open('config/tieba_spider.txt', 'r', encoding='utf-8') as f:
            name = f.readline()
            command_ = command1.format(name, db, days_ago)
            print(command_)
            os.system(command_)
        with open('config/weibo_spider.txt', 'r', encoding='utf-8') as f:
            name = f.readline()
            command_ = command2.format(name, db)
            print(command_)
            os.system(command_)
    except Exception as e:
        print("主进程出错 ==> {}".format(e))
        
def main(db, days_ago):
    sched = BlockingScheduler()
    run(db, days_ago)
    sched.add_job(run, 'cron', hour=0, minute=10, args=[db, days_ago])
    sched.start()
    
            
# 主进程函数
# python -m main
# python -m main --db=01 --days_ago=3
if __name__ == "__main__":
    fire.Fire(main)
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import time

# 实例化一个调度器 后台任务
# BlockingScheduler 阻塞式任务
# AsyncIOScheduler aio库任务
scheduler = BackgroundScheduler()


def job1():
    print("%s: 定时任务任务" % time.asctime())


# 添加任务并设置触发方式为3s一次
scheduler.add_job(job1, 'interval', seconds=0)

# 开始运行调度器
scheduler.start()
for i in range(10):
    print('主进程')
    time.sleep(1)
scheduler.shutdown()

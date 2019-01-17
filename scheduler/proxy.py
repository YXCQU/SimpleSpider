import time

from db.model import IPInfo, OrderID
from proxy import mp
from proxy.mp import get_mp_ip
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from config import mp_url
import json

"""
定时任务调度
"""


def job_get_order_id():
    """
    定时获得 订单id
    :return:
    """
    order_id = mp.get_order_id()
    OrderID.insert(order_id=order_id, time=int(time.time())).on_conflict_ignore().execute()


def job_get_proxy():
    """
    定时获取代理ip，并保存到数据库
    :return:
    """
    order_id = OrderID.select().order_by(OrderID.time.desc())
    # 订单号初始化 添加一个
    if not order_id.exists():
        job_get_order_id()
    data = get_mp_ip(url=mp_url.format(order_id[0].order_id), types='text')
    # 简单处理下数据格式
    if data:
        try:
            data = data.replace("ip:port", "ip_port")
            data = json.loads(data)
            #  插入重复IP数据时 更新数据
            IPInfo.insert_many(data['result']).on_conflict_replace().execute()
        finally:
            print('定时获取IP')


# 实例化调度器
scheduler_get_proxy = BlockingScheduler()
scheduler_get_id = BackgroundScheduler()

# 定时运行 间隔15s
# 'cron', seconds='*/15'
scheduler_get_proxy.add_job(job_get_proxy, 'interval', seconds=15)
scheduler_get_id.add_job(job_get_order_id, 'interval', hours=5, seconds=5)

# 开始运行调度器
scheduler_get_id.start()
scheduler_get_proxy.start()

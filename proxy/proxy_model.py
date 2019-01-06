from peewee import *
import datetime

db = SqliteDatabase('proxy.db')


class BaseModel(Model):
    class Meta:
        database = db


class IPInfo(BaseModel):
    ip_port = CharField(unique=True, help_text='ip地址、端口')
    http_type = CharField(help_text='协议类型 http/socks')
    check_total_count = IntegerField(default=0, help_text='检测总次数')
    check_success_count = IntegerField(default=0, help_text='检测成功次数')
    check_success_ratio = FloatField(default=0, help_text='检测成功率')
    check_time = CharField(help_text='检测时间')
    protocol_status = CharField(help_text='请求方法 post/get')
    transfer_time = FloatField(default=10, help_text='传输时间')
    ping_time = FloatField(default=5, help_text='响应时间')
    country = CharField(help_text='ip所在地')


db.connect()
# db.create_tables([IPInfo])

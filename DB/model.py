from peewee import *
import json

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
    check_dtime = CharField(help_text='检测时间')
    protocol_status = CharField(help_text='支持post/get')
    transfer_time = FloatField(default=10, help_text='传输时间')
    ping_time = FloatField(default=5, help_text='响应时间')
    country = CharField(help_text='国家')
    isp = CharField(help_text='IP运营商')


# db.is_closed()
db.connect()
# db.create_tables([IPInfo])
data = """[{
    "check_total_count": 12251,
    "check_success_ratio": 0.9938780507713656,
    "protocol_status": "POST",
    "transfer_time": 0.214437,
    "ping_time": 0.040218,
    "check_success_count": 12176,
    "check_dtime": 20190106010047,
    "ip:port": "59.37.163.176:1080",
    "http_type": "Socks4",
    "isp": "电信",
    "country": "中国:广东"
},
    {
        "check_total_count": 1117,
        "check_success_ratio": 0.9982094897045658,
        "protocol_status": "POST",
        "transfer_time": 2.402573,
        "ping_time": 0.440857,
        "check_success_count": 1115,
        "check_dtime": 20190105131019,
        "ip:port": "223.25.99.163:1180",
        "http_type": "Socks4",
        "isp": "null",
        "country": "印度"
    },
    {
        "check_total_count": 1028,
        "check_success_ratio": 0.9931906614785992,
        "protocol_status": "GET/POST",
        "transfer_time": 2.999607,
        "ping_time": 0.286922,
        "check_success_count": 1021,
        "check_dtime": 20190106231130,
        "ip:port": "40.77.23.128:3128",
        "http_type": "HTTPS",
        "isp": "null",
        "country": "美国"
    }]""".replace('ip:port', 'ip_port')

data = json.loads(data)
IPInfo.insert_many(data).on_conflict_ignore().execute()

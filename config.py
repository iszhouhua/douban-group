# -*- coding: UTF-8 -*-

import datetime
import logging.config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s[%(name)s] {%(filename)s:%(lineno)d} -> %(message)s'
)

# 请求头
HEADERS = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/103.0.0.0 Safari/537.36',
    # 填写自己的cookie
    "Cookie": ''
}

# 监控的起始时间(仅在此时间之后发布的帖子才进行监控),默认为今天
START_TIME = datetime.datetime.combine(
    datetime.date.today(), datetime.time.min)

# 需要监控的豆瓣小组集合
GROUP_LIST = [
    {"id": "106955", "name": "深圳租房团", "start_time": START_TIME},
    {"id": "592828", "name": "罗湖租房"},
    {"id": "637628", "name": "深圳租房"},
    {"id": "szsh", "name": "深圳租房"},
    {"id": "609271", "name": "深圳租房"}
]

# 匹配规则,符合其中至少一个条件的才进行推送
MATCH_RULES = [
    r"黄贝岭|湖贝|大剧院|红岭|老街|晒布|翠竹|田贝|水贝|草埔|布吉"
]

# 排除规则,此规则中的内容,即便匹配成功了也不进行推送
EXCLUDE_RULES = [
    r"求租|合租",
    r"\d{4}起"
]

# 租金区间限制(目前只会提取四位数的租金，且有一定概率识别错误)
# 不限制
RENT_RANGE = ()
# 仅推送1-2k的帖子
# RENT_RANGE = (1000, 2000)

# 接口请求间隔(秒),默认10-20秒随机
REQUEST_INTERVAL = (10, 20)

# 监控周期(秒),两次循环中间的间隔时长,默认1小时
WATCH_INTERVAL = 3600

# 消息通知配置
NOTIFY = {
    # 渠道 feishu:飞书 work.weixin:企业微信 dingtalk:钉钉
    "channel": "feishu",
    # 机器人WebHook地址
    "url": ""
}

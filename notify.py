import logging
import re

import requests
from config import MATCH_RULES, EXCLUDE_RULES, NOTIFY, RENT_RANGE


def meet_condition(post, start_time):
    """
    判断是否满足通知条件
    """
    if post["create_time"] <= start_time:
        return False
    if RENT_RANGE and (not post['rent'] or post['rent'] < RENT_RANGE[0] or post['rent'] > RENT_RANGE[1]):
        return False
    text = f'{post["title"]}\n{post["content"]}'
    for rule in MATCH_RULES:
        if re.search(rule, text):
            for ex_rule in EXCLUDE_RULES:
                if re.search(ex_rule, text):
                    return False
            return True
    return False


def send_msg(text):
    """
    推送普通消息
    :param text: 消息内容
    """
    data = channel[NOTIFY["channel"]](text)
    response = requests.post(NOTIFY["url"], json=data)
    logging.info('通知内容:%s\n返回结果:%s', text, response.text)


channel = {
    "feishu": lambda content: {
        "msg_type": "interactive",
        "card": {
            "elements": [
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": content
                    }
                }
            ]
        }
    },
    "work.weixin": lambda content: {
        "msgtype": "markdown",
        "markdown": {
            "content": content
        }
    },
    "dingtalk": lambda content: {
        "msgtype": "markdown",
        "markdown": {
            "title": re.search(r'\[(.*)\]', content).group(1) if re.search(r'\[(.*)\]', content) else '豆瓣租房',
            "text": content.replace('\n', '\n\n')
        }
    }
}

import random
import time

import requests

import notify
from config import HEADERS, REQUEST_INTERVAL
from parse import parse_list, parse_detail


def __get(url):
    response = requests.get(url, headers=HEADERS)
    if response.ok:
        return response.text
    if response.status_code == 404:
        return None
    raise RuntimeError(f'请求[{url}]失败,状态码:{response.status_code},内容:{response.text}')


def crawl_list(group_id, start_time, start=None):
    """获取帖子列表
    :param group_id: 小组ID
    :param start_time: 监控帖子的起始时间
    :param start: 分页参数
    """
    url = f'https://www.douban.com/group/{group_id}/'
    if start:
        url += f'/discussion?start={start}'
    html = __get(url)
    if not html:
        return []
    post_list = parse_list(html)
    posts = [x for x in post_list if x['time'] > start_time]
    if len(post_list) == 0 or len(posts) != len(post_list):
        # 列表没有数据，或者存在时间比start_time小的内容，终止获取帖子列表
        return posts
    time.sleep(random.randint(REQUEST_INTERVAL[0], REQUEST_INTERVAL[1]))
    return post_list + crawl_list(group_id, start_time, start + 25 if start else 50)


def crawl_detail(url, start_time):
    """
    获取帖子详情
    """
    html = __get(url)
    if not html:
        return {}
    post = parse_detail(html)
    if notify.meet_condition(post, start_time):
        msg = f'**标题**：[{post["title"]}]({post["url"]})\n**租金**：{post["rent"]}\n**发布时间**：{post["create_time"]}\n**作者**：[{post["author"]["name"]}]({post["author"]["url"]})\n**内容**：{post["content"]}'
        notify.send_msg(msg)
    return post

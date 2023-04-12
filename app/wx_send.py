#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2023/4/4 15:59
@Author:  ting
@File: wx_send.py
@Software: PyCharm
"""
import requests
import time
import json

from . import app

# 设置公众号的app_id和app_secret
APP_ID = app.config['WECHAT_APPID']
APP_SECRET = app.config['WECHAT_SECRET']

ACCESS_TOKEN_URL = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APP_ID}&secret={APP_SECRET}'

access_token = None
expires_in = 0
last_updated = 0


def refresh_access_token():
    global access_token, expires_in, last_updated
    response = requests.get(ACCESS_TOKEN_URL)
    if response.status_code == requests.codes.ok:
        data = response.json()
        access_token = data.get('access_token')
        expires_in = data.get('expires_in')
        last_updated = time.time()
        print(f'Access token refreshed: {access_token}')
    else:
        print(f'Failed to refresh access token: {response.text}')


def get_access_token():
    global access_token, expires_in, last_updated
    current_time = time.time()
    if not access_token or current_time - last_updated > expires_in - 600:  # refresh 10 minutes before expiration
        refresh_access_token()
    return access_token


# 发送文本消息
def send_text_message(openid, message):
    get_access_token()
    url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={}'.format(access_token)
    data = {
        "touser": openid,
        "msgtype": "text",
        "text": {
            "content": message
        }
    }
    response = requests.post(url, data=json.dumps(data))
    if response.status_code == 200:
        return True
    else:
        return False

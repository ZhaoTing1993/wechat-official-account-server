#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2022/9/15 16:10
@Author:  ting
@File: wxmsg.py
@Software: PyCharm
"""
from wechatpy import parse_message
from wechatpy.replies import TextReply


def msg_handle(data):
    msg = parse_message(data)
    print(msg)
    reply = TextReply(content='text reply', message=msg)
    xml = reply.render()
    return xml

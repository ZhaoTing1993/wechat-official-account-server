#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2022/9/15 16:10
@Author:  ting
@File: wxmsg.py
@Software: PyCharm
"""
from wechatpy import parse_message
from app.message_handler import TextMessageHandler, ImageMessageHandler, UnsupportedMessageHandler
from wechatpy.replies import TextReply


# def msg_handle(data):
#     msg = parse_message(data)
#     print(msg)
#     reply = TextReply(content='text reply\ntest', message=msg)
#     xml = reply.render()
#     return xml
from app.wxtool import set_user_id


def msg_handle(data):
    msg = parse_message(data)
    set_user_id(msg.source)
    print(msg)

    # 根据消息类型创建对应的消息处理类实例
    if msg.type == 'text':
        handler = TextMessageHandler()
    elif msg.type == 'image':
        handler = ImageMessageHandler()
    else:
        handler = UnsupportedMessageHandler()
        # # 其他类型的消息暂不处理
        # return ''

    # 调用消息处理类的 handle_message() 方法进行消息处理
    reply_xml = handler.handle_message(msg)
    return reply_xml
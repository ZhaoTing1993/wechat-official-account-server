#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2023/4/4 17:05
@Author:  ting
@File: message_handler.py
@Software: PyCharm
"""
from wechatpy.replies import TextReply

from app.command_handler import wx_commands


class MessageHandler:
    def handle_message(self, msg):
        pass


class TextMessageHandler(MessageHandler):
    @staticmethod
    def is_command(content):
        # 判断是否为命令类型
        return content.startswith('/')

    def handle_message(self, msg):
        if self.is_command(msg.content):
            # 如果是命令类型，则创建相应的命令处理器实例并调用其 handle_command() 方法进行处理
            command_type = msg.content.split('/')[1]
            handler = wx_commands.create_handler(command_type)
            if handler:
                reply_xml = handler.handle_command(msg.content)
                return reply_xml
            else:
                # 如果是未知命令，则返回错误消息
                reply_xml = TextReply(content='Unknown command: ' + command_type, message=msg).render()
                return reply_xml
        else:
            # 处理普通文本消息
            reply_xml = TextReply(content='普通文本回复', message=msg).render()
            return reply_xml
            pass


class ImageMessageHandler(MessageHandler):
    def handle_message(self, msg):
        # 处理图片消息
        reply_xml = TextReply(content='发来的是图片消息，暂时无法处理... ', message=msg).render()
        return reply_xml
        pass


class UnsupportedMessageHandler(MessageHandler):
    def handle_message(self, msg):
        # 处理图片消息
        reply_xml = TextReply(content='暂不支持的消息类型', message=msg).render()
        return reply_xml
        pass

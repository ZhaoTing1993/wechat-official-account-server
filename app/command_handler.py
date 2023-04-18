#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2023/4/4 17:07
@Author:  ting
@File: command_handler.py
@Software: PyCharm
"""
from app.stock.stock_operations import subscribe_stock, add_position, delete_position, get_position


class CommandHandler:
    def handle_command(self, cmd):
        pass


class CommandAHandler(CommandHandler):
    def handle_command(self, cmd):
        # 处理 /a 命令
        pass


class CommandBHandler(CommandHandler):
    def handle_command(self, cmd):
        # 处理 /b 命令
        pass


class CommandCHandler(CommandHandler):
    def handle_command(self, cmd):
        # 处理 /c 命令
        pass


class StockCommandHandler(CommandHandler):
    def handle_command(self, cmd):
        """
            解析用户输入的命令，并执行相应的操作
            """
        print("进入股票处理器")
        # 将命令按空格分割
        parts = cmd.split()

        # 如果命令参数小于 2，则返回错误提示
        if len(parts) < 2:
            return "请指定要操作的股票代码"

        # 获取命令操作类型和参数
        op_type, *op_args = parts[1:]

        # 定义操作函数字典
        operations = {
            "s": subscribe_stock,
            "a": add_position,
            "d": delete_position,
            "q": get_position,
        }

        # 根据操作类型执行相应的操作
        if op_type in operations:
            operation = operations[op_type]
            ret = operation(*op_args)
            return ret  # "完成"
        else:
            return "无效操作，请输入 s、a、d 或 q"


class CommandFactory:
    def __init__(self):
        self.handlers = {}

    def register(self, command_type, handler_class):
        self.handlers[command_type] = handler_class()

    def create_handler(self, command_type):
        return self.handlers.get(command_type)


wx_commands = CommandFactory()
wx_commands.register('a', CommandAHandler)
wx_commands.register('b', CommandBHandler)
wx_commands.register('c', CommandCHandler)
wx_commands.register('s', StockCommandHandler)

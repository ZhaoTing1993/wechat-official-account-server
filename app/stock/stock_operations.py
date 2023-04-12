#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2023/4/7 9:32
@Author:  ting
@File: stock_operations.py
@Software: PyCharm
"""
from app.db.user_stock import UserStock


def subscribe_stock(code):
    # 将股票代码加入订阅列表，add user_stock 表
    user_stock = UserStock()
    rows = user_stock.select_user_stock("test", code=code)
    if not rows:
        # 插入新的用户股票记录
        row = user_stock.insert_user_stock("test", code)
        print(row)
    pass
    try:
        row = user_stock.insert_user_stock("test", code)
    except ValueError as e:
        print(f"插入持仓记录失败：{e}")

def add_position(code, cost, volume):
    # 将持仓添加到 user_stock 表
    user_stock = UserStock()
    rows = user_stock.select_user_stock("test", code=code)
    if not rows:
        # 插入新的用户股票记录
        row = user_stock.insert_user_stock("test", code)
        print(row)
    else:
        # update
        s_id = rows[0]['id']
        user_stock.update_user_stock(s_id, cost=cost, volume=volume)
    pass


def delete_position(code):
    # 将持仓从 user_stock 表中删除
    user_stock = UserStock()
    user_stock.delete_user_stock_by_user_code("test", code)
    pass


def get_position(code):
    # 从 user_stock 表中获取持仓信息
    # 如果不存在，则返回 None
    user_stock = UserStock()
    rows = user_stock.select_user_stock("test", code=code)
    pass

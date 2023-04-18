#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2023/4/7 9:32
@Author:  ting
@File: stock_operations.py
@Software: PyCharm
"""
import app.db.user_stock as user_stock
from app.stock.stock_report import get_pricereport
from app.wxtool import get_user_id
import pandas as pd


def subscribe_stock(code, cost=0, volume=0):
    # 将股票代码加入订阅列表，add user_stock 表
    print("subscribe:{} {} {} {}".format(get_user_id(), code, cost, volume))
    user_stock.add(get_user_id(), code, cost, volume)
    return "{}订阅成功".format(code)


def add_position(code, cost, volume):
    # 将持仓添加到 user_stock 表
    user_stock.update(get_user_id(), code, cost, volume)
    return "{}持仓更新成功 \n当前成本{} \n持股数{}".format(code, cost, volume)


def delete_position(code):
    # 将持仓从 user_stock 表中删除
    user_stock.delete(get_user_id(), code)
    return "{}成功退订".format(code)


def get_position(code=None):
    # 从 user_stock 表中获取持仓信息
    # 如果不存在，则返回 None
    rows = user_stock.query(get_user_id(), code)
    if rows:
        ret = ""
        # for row in rows:
        #     ret += "{}\t{}\t{}\t{}\t{}\n".format(row.code, row.price, row.cost, row.volume, row.time)
        rows_dict = [{'code': stock.code, 'cost': stock.cost, 'volume': stock.volume} for stock in rows]
        # Convert rows to a DataFrame
        df = pd.DataFrame(rows_dict, columns=['code', 'cost', 'volume'])
        # Rename the 'volume' column to 'vol'
        # df = df.rename(columns={'volume': 'vol'})
        dict_df = df.to_dict('list')
        result_dict = {
            'code': [str(c) for c in dict_df['code']],
            'cost': [str(c) for c in dict_df['cost']],
            'vol': [str(v) for v in dict_df['volume']]
        }
        print(result_dict)
        report_data = get_pricereport(result_dict)
        row_count = report_data.shape[0]
        for i in range(row_count):
            ret += "------------\n"
            ret += f"代码: {report_data.iloc[i]['code']}\n名称: {report_data.iloc[i]['name']}\n价格: {report_data.iloc[i]['price']}\n成本: {report_data.iloc[i]['cost']}\n持仓: {report_data.iloc[i]['vol']}\n利润: {report_data.iloc[i]['prof']}\n利润率: {report_data.iloc[i]['prof_percent']}\n"
        print(ret)
        return ret
    else:
        return "暂无持仓"

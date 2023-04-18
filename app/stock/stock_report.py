#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2022/9/16 16:37
@Author:  ting
@File: stock_report.py
@Software: PyCharm
"""
import pandas as pd
import tushare as ts

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_rows', None)

stock_df = {
    'code': ['000554', '002235', '002712', '000608'],
    'cost': ['5.960', '4.827', '4.857', '3.085'],
    'vol': ['500', '700', '700', '1000']
}


def get_pricereport(stock_df):
    df = ts.get_realtime_quotes(stock_df['code'])
    df['cost'] = stock_df['cost']
    df['vol'] = stock_df['vol']
    df['prof'] = df[['price', 'cost', 'vol']].apply(
        lambda x: round(float(x['vol']) * (float(x['price']) - float(x['cost'])), 2),
        axis=1)
    df['percent'] = df[['price', 'open']].apply(
        lambda x: f"{round(((float(x['price']) - float(x['open'])) / float(x['price'])) * 100, 2)}%",
        axis=1)
    df['prof_percent'] = df[['price', 'cost']].apply(
        lambda x: f"{round(((float(x['price']) - float(x['cost'])) / float(x['cost'])) * 100, 2)}%",
        axis=1)
    print(df[['name', 'code', 'price', 'cost', 'vol', 'prof', 'prof_percent']])
    print(df['prof'].sum())
    return df


if __name__ == '__main__':
    # get_pricereport(stock_df)
    ret = ""
    report_data = get_pricereport(stock_df)
    row_count = report_data.shape[0]
    for i in range(row_count):
        ret += "------------\n"
        ret += f"Code: {report_data.iloc[i]['code']}\nPrice: {report_data.iloc[i]['price']}\nCost: {report_data.iloc[i]['cost']}\nVolume: {report_data.iloc[i]['vol']}\nProfit: {report_data.iloc[i]['prof']}\nProfit Percentage: {report_data.iloc[i]['prof_percent']}\n"
    print(ret)

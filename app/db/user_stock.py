#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2023/4/4 16:37
@Author:  ting
@File: user_stock.py
@Software: PyCharm
"""
import datetime
from decimal import Decimal

import sqlalchemy

from app.db.db_config import my_db


def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance


@singleton
class UserStock:
    def __init__(self):
        # 定义用户股票表(user_stock)模型
        self.user_stock = sqlalchemy.Table(
            "user_stock",
            sqlalchemy.MetaData(),
            sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
            sqlalchemy.Column("user", sqlalchemy.String),
            sqlalchemy.Column("code", sqlalchemy.Integer),
            sqlalchemy.Column("cost", sqlalchemy.Numeric),
            sqlalchemy.Column("volume", sqlalchemy.Integer),
            sqlalchemy.Column("create_time", sqlalchemy.DateTime),
            sqlalchemy.Column("update_time", sqlalchemy.DateTime),

            sqlalchemy.UniqueConstraint("user", "code")
        )

        self.database = my_db

    def create_table(self):
        """
        创建用户股票表。
        """
        with self.database.engine.begin() as conn:
            if not conn.run_sync(self.user_stock.exists):
                conn.run_sync(self.user_stock.create)

    def get_user_stock(self, **filters):
        """
        查询符合过滤条件的用户股票记录。
        """
        query = self.user_stock.select()

        for key, value in filters.items():
            if hasattr(self.user_stock.c, key):
                column = getattr(self.user_stock.c, key)
                query = query.where(column == value)

        row = self.database.fetch_one(query)

        if not row:
            return None

        return dict(row)

    def insert_user_stock(self, user, code, **kwargs):
        """
        插入一条新的用户股票记录，
        只有表格中user和code为联合唯一，只有user和code不存在时可以插入。
        """
        # 检查 user 和 code 是否存在于数据库中
        record = self.get_user_stock(user=user, code=code)
        if record:
            raise ValueError(f"用户 {user} 已经存在股票 {code} 的持仓记录")

        now = datetime.datetime.now()

        values = {
            "user": user,
            "code": code,
            "create_time": now,
            "update_time": now,
        }

        values.update({k: Decimal(v) for k, v in kwargs.items() if k == "cost"})
        values.update({k: int(v) for k, v in kwargs.items() if k == "volume"})

        query = (
            self.user_stock.insert()
                .values(**values)
                .returning(self.user_stock)
        )

        row = self.database.fetch_one(query)
        return dict(row)

    def select_user_stock(self, user, **filters):
        """
        查询指定用户符合过滤条件的所有股票记录。
        """
        query = self.user_stock.select().where(self.user_stock.c.user == user)

        for key, value in filters.items():
            if hasattr(self.user_stock.c, key):
                column = getattr(self.user_stock.c, key)
                query = query.where(column == value)

        rows = self.database.fetch_all(query)

        return [dict(row) for row in rows]

    def update_user_stock(self, id_, user=None, code=None, cost=None, volume=None):
        """
        更新指定ID的股票记录。
        """
        query = (
            self.user_stock.update()
                .where(self.user_stock.c.id == id_)
                .values(
                {
                    "user": user,
                    "code": code,
                    "cost": Decimal(cost) if cost is not None else None,
                    "volume": volume,
                    "update_time": datetime.datetime.now(),
                }
            )
                .returning(self.user_stock)
        )

        row = self.database.fetch_one(query)

        return dict(row)

    def delete_user_stock(self, id_):
        """
        删除指定ID的股票记录。
        """
        query = self.user_stock.delete().where(self.user_stock.c.id == id_)
        self.database.execute(query)

    def delete_user_stock_by_user_code(self, user: str, code: int):
        query = self.user_stock.delete().where(
            sqlalchemy.and_(
                self.user_stock.c.user == user,
                self.user_stock.c.code == code
            )
        )
        self.database.execute(query)


def example():
    user_stock = UserStock()

    # 创建用户股票表
    user_stock.create_table()

    # 插入新的用户股票记录
    row = user_stock.insert_user_stock("test", 1234, 12.34, 123.4, 100)
    print(row)

    # 查询指定用户的所有股票记录
    filter = {'code': 600001}
    rows = user_stock.select_user_stock("test", filter)
    print(rows)

    # 更新指定ID的股票记录
    row = user_stock.update_user_stock(1, cost=23.45, volume=200)
    print(row)

    # 删除指定ID的股票记录
    user_stock.delete_user_stock(1)
    user_stock.delete_user_stock_by_user_code("test", 600001)

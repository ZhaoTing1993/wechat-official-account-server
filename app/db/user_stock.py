#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2023/4/4 16:37
@Author:  ting
@File: user_stock.py
@Software: PyCharm
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Numeric, MetaData
from sqlalchemy.ext.declarative import declarative_base
from app.db.db_config import Session, engine

# 创建Base对象

Base = declarative_base()


# 定义UserStock对象
class UserStock(Base):
    __tablename__ = 'user_stock'

    id = Column(Integer, primary_key=True)
    user = Column(String(255), nullable=False)
    code = Column(Integer, nullable=False)
    price = Column(Numeric(precision=20, scale=2), nullable=False)
    cost = Column(Numeric(precision=20, scale=2), nullable=False)
    volume = Column(Integer, nullable=False)
    create_time = Column(DateTime, nullable=False, default=datetime.now)
    update_time = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)


# 创建用户股票表
def create_user_stock_table():
    # 获取元数据对象
    metadata = MetaData()

    # 如果表已存在则不创建
    if metadata.tables.get('user_stock') is not None:
        return

    # 创建表
    Base.metadata.create_all(engine)


# 查询所有记录
def query_all():
    session = Session()
    stocks = session.query(UserStock).all()
    session.close()
    return stocks


# 根据条件查询记录
def query(user, code=None):
    session = Session()
    if code:
        stocks = session.query(UserStock).filter(UserStock.user == user, UserStock.code == code).all()
    else:
        stocks = session.query(UserStock).filter(UserStock.user == user).all()
    session.close()
    return stocks


# 新增一条记录
def add(user, code, price=0, cost=0, volume=0):
    session = Session()
    new_stock = UserStock(user=user, code=code, price=price, cost=cost, volume=volume)
    session.add(new_stock)
    session.commit()
    session.close()


# 更新一条记录
def update(user, code, volume=None, price=None, cost=None):
    session = Session()
    stock = session.query(UserStock).filter_by(user=user, code=code).first()
    if volume is not None:
        stock.volume = volume
    if price is not None:
        stock.price = price
    if cost is not None:
        stock.cost = cost
    stock.update_time = datetime.now()
    session.commit()
    session.close()


# 删除一条记录
def delete(user, code):
    session = Session()
    stock = session.query(UserStock).filter_by(user=user, code=code).first()
    session.delete(stock)
    session.commit()
    session.close()

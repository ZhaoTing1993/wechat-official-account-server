#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2023/4/4 16:33
@Author:  ting
@File: db_config.py
@Software: PyCharm
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app


db_host = app.config.get("DB_HOST", "localhost")
db_port = app.config.get("DB_PORT", "3306")
db_user = app.config.get("DB_USER", "admin")
db_password = app.config.get("DB_PASSWORD", "admin")
db_name = app.config.get("DB_NAME", "flask_demo")
db_charset = app.config.get("DB_CHARSET", "utf8mb4")


DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?charset={db_charset}"

# 创建数据库连接引擎
engine = create_engine(DATABASE_URL, pool_recycle=3600,
                       pool_size=10)

# 创建Session工厂类
Session = sessionmaker(bind=engine)

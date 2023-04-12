#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2023/4/4 16:33
@Author:  ting
@File: db_config.py
@Software: PyCharm
"""
import databases
import sqlalchemy

# 根据所选数据库的不同，可能需要使用不同的Python库来进行连接。如果选择使用MySQL，则需要使用pymysql库；如果选择使用SQLite，则需要使用sqlite3库。
# "sqlite:///example.db"
# "mysql+pymysql://user:password@server:port/dbname"
# "postgresql://user:password@localhost/dbname"

DATABASE_URL = "sqlite:///example.db"

# 创建数据库连接引擎
engine = sqlalchemy.create_engine(
    DATABASE_URL, pool_size=10, max_overflow=20, pool_recycle=300
)

# 创建数据库连接实例
my_db = databases.Database(DATABASE_URL, force_rollback=False)


async def connect_to_database():
    """
    连接数据库并创建连接池，并在应用启动时调用此函数。
    """
    await my_db.connect()


async def close_database_connection():
    """
    关闭数据库连接，并在应用结束时调用此函数。
    """
    await my_db.disconnect()

#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2022/9/15 11:09
@Author:  ting
@File: __init__.py.py
@Software: PyCharm
"""

from flask import Flask

import config

app = Flask(__name__, instance_relative_config=True)
# 加载配置
app.config.from_object('config')
app.config.from_pyfile('config.py')

from .wxctl import bp as wx_bp

app.register_blueprint(wx_bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2022/9/15 11:22
@Author:  ting
@File: wxctl.py
@Software: PyCharm
"""

from flask import Blueprint

from . import app

bp = Blueprint('wx', __name__, url_prefix='/wx')


@app.route("/", methods=['GET', 'POST'])
def wx():

    return 'succ'

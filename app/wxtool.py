#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2022/9/15 13:47
@Author:  ting
@File: wxtool.py
@Software: PyCharm
"""
from functools import wraps

from flask import request, abort
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.utils import check_signature

from . import app

TOKEN = app.config['WECHAT_TOKEN']


def wx_signature(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        signature = request.args.get('signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        try:
            check_signature(TOKEN, signature, timestamp, nonce)
        except InvalidSignatureException:
            print("InvalidSignatureException")
            abort(400)
        return func(*args, **kwargs)

    return decorated_function

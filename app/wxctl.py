#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2022/9/15 11:22
@Author:  ting
@File: wxctl.py
@Software: PyCharm
"""

from flask import Blueprint, request, abort

from .wxtool import wx_signature
from .wxmsg import msg_handle

bp = Blueprint('wxctl', __name__, url_prefix='/wx')


@bp.route("/", methods=['GET', 'POST'])
@wx_signature
def wx():
    if request.method == 'GET':
        echostr = request.args.get('echostr', '')
        return echostr
    elif request.method == 'POST':
        return msg_handle(request.data)
    else:
        abort(400)

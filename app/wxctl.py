#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2022/9/15 11:22
@Author:  ting
@File: wxctl.py
@Software: PyCharm
"""

from flask import Blueprint, request, abort, Response

from .wx_send import send_text_message
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
        xml_ret = msg_handle(request.data)
        return Response(xml_ret, content_type="application/xml")
    else:
        abort(400)


@bp.route("/send", methods=['GET', 'POST'])
@wx_signature
def send():
    if request.method == 'GET':
        text = request.args.get('text', '')
        send_text_message('oP1qd6SekcTdG5lOOf_zYO9Wyo8g', text)

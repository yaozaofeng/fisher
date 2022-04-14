"""
 Created by 七月 on 2018-4-4.
"""
__author__ = '七月'

from flask import Flask, current_app

app = Flask(__name__)

ctx = app.app_context()
ctx.push()
a = current_app
d = a
 
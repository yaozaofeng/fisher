"""
 Created by 七月 on 2018-2-6.
"""
__author__ = '七月'

from flask import Flask, current_app, request, Request

app = Flask(__name__)
# 应用上下文 对象 Flask
# 请求上下文 对象 Request
# Flask AppContext
# Request RequestContext
# 离线应用、单元测试
# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()

with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']


# 文件读写
# try:
#     f = open(r'D:\t.txt')
#     print(f.read())
# finally:
#     f.close()
#
# with open(r'') as f:
#     print(f.read())
# 1. 连接数据库
# 2. sql
# 3. 释放资源
#
# __enter__
# __exit__
# try
# except
# finally:

# 实现了上下文协议的对象使用with
# 上下文管理器
# __enter__ __exit__
# 上下文表达式必须要返回一个上下文管理器
# with


class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if tb:
            print('process exception')
        else:
            print('no exception')
        print('close resource connection')

    def query(self):
        print('query data')


try:
    with MyResource() as resource:
        1 / 0
        resource.query()
except Exception as ex:
    pass

# 开发时间： 2022/3/26 $ 14:30
from flask import Flask

__author__ = 'yaozaofeng'

from app.__init__ import create_app

app = create_app()

if __name__ == '__main__':
    # 生产环境 nginx + uwsgi
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=8181)

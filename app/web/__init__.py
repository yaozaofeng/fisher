# 开发时间： 2022/3/28 $ 21:12
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book
from app.web import user
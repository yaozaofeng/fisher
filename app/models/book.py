# 开发时间： 2022/3/29 $ 18:29
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))  # 精装 or 板装
    publisher = Column(String(50))  # 出版社
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))  # 出版年月
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))  # 简介
    image = Column(String(50))

    def sample(self):
        pass

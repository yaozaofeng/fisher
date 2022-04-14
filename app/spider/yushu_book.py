# 开发时间： 2022/3/28 $ 14:18

from app.libs.httper import HTTP
from flask import current_app


class YuShuBook:
    # 模型层 MVC M层
    isbn_url = 'http://t.talelin.com/v2/book/isbn/{}'
    keyword_url = 'http://t.talelin.com/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = YuShuBook.isbn_url.format(isbn)
        result = HTTP.get(url)

        # dict
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = YuShuBook.keyword_url.format(keyword, current_app.config['PER_PAGE'],
                                           cls.calculate_start(page))
        result = HTTP.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']

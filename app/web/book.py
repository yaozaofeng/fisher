# 开发时间： 2022/3/28 $ 16:18
from flask import jsonify, request

from app.libs.Helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web
from ..forms.book import SearchForm


@web.route('/book/search')
def search():
    """
    :param q: 普通关键字 isbn
    :param page:
    :param ?q=金庸&page=1
    """
    # 验证层 forms
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)
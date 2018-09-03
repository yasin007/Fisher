"""
create by 维尼的小熊 on 2018/9/3

"""
from flask import jsonify, request
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web
from app.forms.book import SearchForm

__autor__ = 'yasin'


@web.route('/book/search')
def search():
    # q = request.args['q']
    # page = request.args['page']

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
            print(result)
        return jsonify(result)
    else:
        return jsonify(form.errors)

"""
create by 维尼的小熊 on 2018/9/3

"""
__autor__ = 'yasin'

from app.libs.http import Http
from flask import current_app


class YuShuBook:
    per_page = 15
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = Http.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = Http.get(url)
        return result

    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']

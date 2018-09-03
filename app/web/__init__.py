"""
create by 维尼的小熊 on 2018/9/3

"""
from flask import Blueprint

__autor__ = 'yasin'

web = Blueprint('web', __name__)

from app.web import book
from app.web import user

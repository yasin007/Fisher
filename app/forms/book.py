"""
create by 维尼的小熊 on 2018/9/3

"""
__autor__ = 'yasin'

from wtforms import Form, StringField, IntegerField
from wtforms.validators import length, number_range, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), length(min=1, max=30, message='请输入1到30位的字符串')])
    page = IntegerField(validators=[number_range(min=1, max=99, message='请输入1到99的分页码')], default=1)

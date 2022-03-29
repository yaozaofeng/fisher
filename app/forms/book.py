# 开发时间： 2022/3/29 $ 15:42
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


# wtforms - 参数校验
class SearchForm(Form):
    q = StringField(validators=[DataRequired(),Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Optional, Regexp


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[URL(), DataRequired()]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Regexp(r'^[a-zA-Z0-9]{1,16}$'),
            Optional(strip_whitespace=False),
        ],
    )
    submit = SubmitField('Создать')
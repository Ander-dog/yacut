from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from settings import SHORT_ID_MAX_LENGTH, SHORT_ID_REGEX


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[URL(), DataRequired()]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Regexp(SHORT_ID_REGEX),
            Optional(strip_whitespace=False),
            Length(max=SHORT_ID_MAX_LENGTH),
        ],
    )
    submit = SubmitField('Создать')
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Optional, Regexp, Length

from settings import SHORT_ID_REGEX, SHORT_ID_MAX_LENGTH


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
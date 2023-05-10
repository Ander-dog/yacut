import string
from datetime import datetime
from random import choice

from flask import url_for

from settings import SHORT_ID_LENGTH, SHORT_ID_MAX_LENGTH

from . import db


def generate_short_id(length):
    letters = string.digits + string.ascii_letters
    short = ''.join(choice(letters) for i in range(length))
    while URLMap.query.filter_by(short=short).first() is not None:
        short = ''.join(choice(letters) for i in range(length))
    return short


def get_unique_short_id(short):
    if short is None or short == '':
        short = generate_short_id(SHORT_ID_LENGTH)
    return short


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(
        db.String(SHORT_ID_MAX_LENGTH),
        unique=True,
        nullable=False
    )
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                'redirect_view',
                short=self.short,
                _external=True
            )
        )

import string
from datetime import datetime
from random import choice

from flask import url_for

from . import db


def get_unique_short_id(short):
    if short is None or short == '':
        letters = string.digits + string.ascii_letters
        short = ''.join(choice(letters) for i in range(6))
        while URLMap.query.filter_by(short=short).first() is not None:
            short = ''.join(choice(letters) for i in range(6))
    return short


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, unique=True, nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
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

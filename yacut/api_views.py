import re

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap, get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def add_id():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    short = data.get('custom_id', None)
    if short and not re.match(r'^[a-zA-Z0-9]{1,16}$', short):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if short and URLMap.query.filter_by(short=short).first():
        raise InvalidAPIUsage(f'Имя "{short}" уже занято.')
    url_map = URLMap(
        original=data['url'],
        short=get_unique_short_id(short))
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), 201


@app.route('/api/id/<short>/', methods=['GET'])
def get_id(short):
    url_map = URLMap.query.filter_by(short=short).first()
    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': url_map.original}), 200

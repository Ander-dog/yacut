from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap, get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()

    if form.validate_on_submit():
        original = form.original_link.data
        short = form.custom_id.data

        if URLMap.query.filter_by(short=short).first():
            flash(f'Имя {short} уже занято!')
            return render_template('index.html', form=form)
        elif URLMap.query.filter_by(original=original).first():
            flash('Для такого url уже есть короткая ссылка:')
            url_map = URLMap.query.filter_by(original=original).first()
        else:
            flash('Ваша новая ссылка готова:')
            url_map = URLMap(
                original=original,
                short=get_unique_short_id(short)
            )
            db.session.add(url_map)
            db.session.commit()

        new_url = url_for(
            'redirect_view',
            short=url_map.short,
            _external=True
        )
        return render_template('index.html', form=form, new_url=new_url)

    return render_template('index.html', form=form)


@app.route('/<short>', methods=['GET'])
def redirect_view(short):
    url_map = URLMap.query.filter_by(short=short).first()
    if url_map is not None:
        return redirect(url_map.original)
    abort(404)

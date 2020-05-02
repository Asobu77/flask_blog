# flask_blog/views.py

# 必要なパッケージをインポート
from flask import request, redirect, url_for, render_template, flash, session, Blueprint
# __init__.pyで作成したappをインポートする
from flask_blog import app, db
from flask_blog.models.weights import Weight
from flask_blog.views.views import login_required

import datetime

weight = Blueprint('weight', __name__)

@weight.route('/new', methods=['GET'])
@login_required
def new():
    defalut = dict(date = datetime.date.today())
    return render_template('weights/new.html', weights = defalut)

@weight.route('/register', methods=['POST'])
def register():
    req_date   = request.form['date']
    req_weight = request.form['weight']

    if not req_date or not req_weight:
        flash('全ての項目を記入してください')
        return render_template('weights/new.html', weights = request.form)

    weight = Weight(
        user_id = session.get('login_user'),
        date    = req_date,
        weight  = req_weight
    )
    db.session.add(weight)
    db.session.commit()

    flash('体重を記録しました')
    defalut = dict(date = datetime.date.today())
    return render_template('weights/new.html', weights = defalut)



# @entry.route('/entries/new', methods=['GET'])
# @login_required
# def new_entry():
#     return render_template('entries/new.html')

# @entry.route('/entries', methods=['POST'])
# @login_required
# def add_entry():
#     entry = Entry(
#         title = request.form['title'],
#         text  = request.form['text']
#     )
#     db.session.add(entry)
#     db.session.commit()
#     flash('新しい記事が作成されました')
#     return redirect(url_for('entry.show_entries'))

# @entry.route('/entries/<int:id>', methods=['GET'])
# @login_required
# def show_entry(id):
#     entry = Entry.query.get(id)
#     return render_template('entries/show.html', entry = entry)
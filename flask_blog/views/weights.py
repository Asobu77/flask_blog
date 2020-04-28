# flask_blog/views.py

# 必要なパッケージをインポート
from flask import request, redirect, url_for, render_template, flash, session, Blueprint
# __init__.pyで作成したappをインポートする
from flask_blog import app, db
from flask_blog.models.weights import Weight
from flask_blog.views.views import login_required

weight = Blueprint('weight', __name__)

@weight.route('/new', methods=['GET'])
@login_required
def new():
    return render_template('weights/new.html', weights = None)

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
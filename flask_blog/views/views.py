# flask_blog/views.py

# 必要なパッケージをインポート
from flask import request, redirect, url_for, render_template, flash, session, Blueprint
# __init__.pyで作成したappをインポートする
from flask_blog import app, db
from flask_blog.models.users import User
from functools import wraps
import sys

view = Blueprint('view', __name__)

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('view.login'))
        return view(*args, **kwargs)
    return inner

@view.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_user = User.query.filter( \
            User.mail_address == request.form['mail_address'], \
            User.password == request.form['password'] \
            ).first()
        if not login_user:
            flash('パスワードもしくはメールアドレスが異なります')
        else:
            # session更新
            session['logged_in']     = True
            session['login_user_id']   = login_user.id
            session['login_user_name'] = login_user.user_name

            # 下記はデバックで使用する
            # app.logger.debug(session)

            flash('ログインしました')
            return redirect(url_for('entry.show_entries'))
    return render_template('login.html')

@view.route('/logout')
def logout():
    # session削除
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('view.login'))

# errorhanderイベントをBlueprintで使用する場合はapp_errorhandlerを使う
@view.app_errorhandler(404)
def non_route(error):
    # 一覧画面に遷移
    return redirect(url_for('entry.show_entries'))


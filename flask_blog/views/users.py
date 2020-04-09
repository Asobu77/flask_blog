from flask import request, redirect, url_for, render_template, flash, session, Blueprint
from flask_blog import app, db
from flask_blog.models.users import User
import sys


user = Blueprint('user', __name__)

@user.route('/new', methods=['GET'])
def new():
    return render_template('users/new.html', form = '')

@user.route('/register', methods=['POST'])
def register():
    user_name    = request.form['user_name']
    mail_address = request.form['mail_address']
    password     = request.form['password']

    # Nullチェック
    if not user_name or not mail_address or not password:
        flash('全ての項目を記入してください')
        return render_template('users/new.html', form = request.form)

    # 文字数チェック
    if not len(user_name) <= 30:
        flash('氏名は30文字以内で記入してください')
        return render_template('users/new.html', form = request.form)

    if not len(mail_address) <= 50:
        flash('メールアドレスは50文字以内で記入してください')
        return render_template('users/new.html', form = request.form)

    if not len(password) <= 30:
        flash('パスワードは30文字以内で記入してください')
        return render_template('users/new.html', form = request.form)

    # メールアドレス重複チェック
    is_exists = User.query.filter(User.mail_address == mail_address).count()
    if 0 < is_exists:
        flash(is_exists)
        return render_template('users/new.html', form = request.form)

    # 登録
    user = User(
        user_name    = request.form['user_name'],
        mail_address = request.form['mail_address'],
        password     = request.form['password']
    )
    db.session.add(user)
    db.session.commit()

    flash('ユーザーを登録しました')
    return redirect(url_for('view.login'))

# # errorhanderイベントをBlueprintで使用する場合はapp_errorhandlerを使う
# @view.app_errorhandler(404)
# def non_route(error):
#     # 一覧画面に遷移
#     return redirect(url_for('entry.show_entries'))


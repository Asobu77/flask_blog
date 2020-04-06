# flask_blog/views.py

# 必要なパッケージをインポート
from flask import request, redirect, url_for, render_template, flash, session
# __init__.pyで作成したappをインポートする
from flask_blog import app
import sys

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザー名が異なります')
        elif request.form['username'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            # session更新
            session['logged_in'] = True
            flash('ログインしました')
            return redirect(url_for('show_entries'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    # session削除
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))


# flask_blog/views.py

# __init__.pyで作成したappをインポートする
from flask_blog import app

# 必要なパッケージをインポート
from flask import request, redirect, url_for, render_template, flash, session
import sys

@app.route('/')
def show_entries():
    # セッションがなければログインする
    if not session.get('logged_in'):
        return redirect('/login')

    return render_template('entries/index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            print('ユーザー名が異なります')
        elif request.form['username'] != app.config['PASSWORD']:
            print('パスワードが異なります')
        else:
            # session更新
            session['logged_in'] = True
            return redirect('/')

    return render_template('login.html')

@app.route('/logout')
def logout():
    # session削除
    session.pop('logged_in', None)
    return redirect('/')


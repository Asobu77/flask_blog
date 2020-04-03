# flask_blog/views.py

# __init__.pyで作成したappをインポートする
from flask_blog import app

# 必要なパッケージをインポート
from flask import request, redirect, url_for, render_template, flash, session


@app.route('/')
def show_entries():
    return render_template('entries/index.html')

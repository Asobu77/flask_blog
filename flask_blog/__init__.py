# flask_blog/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# アプリケーション本体を作成。らしい。
app = Flask(__name__)
# config.pyの内容をconfigとして扱う
app.config.from_object('flask_blog.config')

# db
db = SQLAlchemy(app)


import flask_blog.views
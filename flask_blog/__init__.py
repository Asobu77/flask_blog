# coding: UTF-8
# flask_blog/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# アプリケーション本体を作成。らしい。
app = Flask(__name__)

# config.pyの内容をconfigとして扱う
app.config.from_object('flask_blog.config')

# db
db = SQLAlchemy(app)

# Blueprintで分割した機能を登録する
from flask_blog.views.entries import entry
app.register_blueprint(entry, url_prefix='/article')

from flask_blog.views.views import view
app.register_blueprint(view)

from flask_blog.views.users import user
app.register_blueprint(user, url_prefix='/user')

from flask_blog.views.weights import weight
app.register_blueprint(weight, url_prefix='/weight')

from flask_blog.views.dashboard import dashboard
app.register_blueprint(dashboard, url_prefix='/dashboard')

if __name__ == '__main__':
    app.run(debug = True)
# coding: UTF-8
# server.py
from flask_blog import app

# このファイルが直接実行されたときの処理をTureケースに書き込む
if __name__ == '__main__':
    app.run(debug = True)

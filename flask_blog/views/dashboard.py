from flask import request, redirect, url_for, render_template, flash, session, Blueprint
from flask_blog import app, db
from flask_blog.models.weights import Weight
from flask_blog.models.users import User
from flask_blog.views.views import login_required
from sqlalchemy import and_
import datetime, time, sys

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/', methods=['GET'])
@login_required
def top():
    print(app.config['TEST_CONFIG'])

    # クエリ
    # 半年以内のデータを抽出
    from_date = request.args.get('from_date') if request.args.get('from_date') else datetime.date.today()
    to_date   = request.args.get('to_date') if request.args.get('to_date') else datetime.date.today()

    filters = []
    filters.append(Weight.date >= from_date)
    filters.append(Weight.date <= to_date)

    Weights = Weight.query.\
        filter(Weight.user_id == session.get('login_user_id')).\
        filter(and_(*filters)).\
        order_by(Weight.date.asc()).\
        all()

    # データをリストに格納していく
    recode_date   = list()
    recode_weight = list()

    for i in Weights:
        recode_date.append(datetime.datetime.strftime(i.date, "%m/%d"))
        recode_weight.append(i.weight)
    data   = { 'date' : recode_date, 'weight' : recode_weight, 'name' : session.get('login_user_name') }
    period = { 'from_date' : from_date, 'to_date' : to_date }

    return render_template('dashboard/top.html', data = data, period = period)


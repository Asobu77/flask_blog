from flask import request, redirect, url_for, render_template, flash, session, Blueprint
from flask_blog import app, db
from flask_blog.models.weights import Weight
from flask_blog.views.views import login_required
import datetime
import sys

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/', methods=['GET'])
@login_required
def top():
    # データをリストに格納していく
    recode_date = list()
    recode_weight = list()
    Weights = Weight.query.order_by(Weight.date.asc()).all()
    for i in Weights:
        recode_date.append(datetime.datetime.strftime(i.date, "%m/%d"))
        recode_weight.append(i.weight)
    app.logger.debug(recode_date)
    data = { 'date' : recode_date, 'weight' : recode_weight }
    return render_template('dashboard/top.html', data = data)

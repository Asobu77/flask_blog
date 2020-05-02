from flask import request, redirect, url_for, render_template, flash, session, Blueprint
from flask_blog import app, db
from flask_blog.models.weights import Weight
from flask_blog.views.views import login_required

import sys

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/', methods=['GET'])
@login_required
def top():
    return render_template('dashboard/top.html')

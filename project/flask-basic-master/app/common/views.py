from flask import Blueprint, render_template
from flask_user import login_required


@login_required
def index():
    return render_template('common/index.html')

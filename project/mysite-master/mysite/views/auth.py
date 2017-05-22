from flask import Blueprint, render_template, url_for, request
from flask.ext.login import login_required, login_user, redirect, logout_user, current_user
from ..forms import LoginForm
from ..models import db, User
from ..utils import ldap_verify_user, ldap_query_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    next = request.args.get('next', url_for('main.index'))
    if current_user.is_authenticated():
        return redirect(next)

    form = LoginForm()
    if form.validate_on_submit():
        core_id = form.core_id.data
        password = form.password.data
        # if ldap_verify_user(core_id, password):
        #     user = User.get(core_id)
        #     if not user:
        #         data = ldap_query_user(core_id, 'displayName', 'mail')
        #         assert data is not None
        #         user = User(core_id, data['displayName'], data['mail'])
        #         db.session.add(user)
        #         db.session.commit()
        #     login_user(user)
        #     return redirect(next)
        user = User.get(core_id)
        login_user(user)
        return redirect(next)
    return render_template('auth/login.html', form=form, next=next)


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

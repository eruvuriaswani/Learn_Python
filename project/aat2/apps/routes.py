from apps import app
from flask import (render_template, request, flash, session,
                   url_for, redirect, jsonify)
from werkzeug.utils import secure_filename
from apps import login_manager
from flask_login import login_required, login_user, logout_user
import json
import os
import string
import random

from .forms import SigninForm, RegistrationForm
from .models import db, User, Project, ApiRequests
from .config import ALLOWED_EXTENSIONS
from .utils import uploadFile, nocache


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# TEST CASES SECTION
@app.route("/get_tcs", methods=['GET'])
@login_required
def get_tcs():
    pass


@app.route("/get_my_projects", methods=['GET'])
@login_required
def get_my_projects():
    return json.dumps(User.get_projects(session['user_id']))

# TEST CASES SECTION ENDS


@app.route('/login')
def login():
    signin_form = SigninForm()
    return render_template('v2/login.html',
                           form=signin_form)


@app.route('/')
@login_required
def home():
    return render_template('gentella/dashboard.html')


@app.route('/run')
@login_required
def run():
    project_dict = User.get_projects(session['user_id'])
    return render_template('gentella/run.html',
                           projects=project_dict,
                           username="johri_m@hcl.com",
                           testcases=[{"name": "Check the Register"},
                                      {"name": "New Test for Register"}])


@app.route("/get_free_apis", methods=['GET'])
# @login_required
# @nocache
def get_free_apis():
    project_id = request.args.get('proj')
    d = db.session.query(ApiRequests) \
                  .filter_by(project_id=project_id) \
                  .filter_by(flag_used=False) \
                  .options(db.load_only('id', "url")).all()
    return jsonify(data=[(False, a.id, a.url) for a in d])
    # return jsonify(data=[{'id': a.id, 'url': a.url} for a in d])


@app.route("/get_free_apis_by_prj_name", methods=['GET'])
@login_required
@nocache
def get_free_apis_by_prj_name():
    proj = request.args.get('proj')
    proj = Project.query.filter_by(name=proj).first()
    d = db.session.query(ApiRequests) \
                  .filter_by(project_id=proj.id) \
                  .filter_by(flag_used=False) \
                  .options(db.load_only('id', "url")).all()
    return jsonify(data=[(a.id, a.id, a.url) for a in d])


@app.route("/create_tcs", methods=['POST'])
@login_required
@nocache
def create_tcs():
    data = request.form
    print("data>", data)
    for d in data.getlist('apis'):
        print(d)
    return("{result: True}")


@app.route("/uploaded_file", methods=['GET'])
# @login_required
@nocache
def uploaded_file():
    project_dict = User.get_projects(session['user_id'])
    return render_template("v2/process_apis.html", projects=project_dict)


@app.route("/remove_apis", methods=['POST'])
@nocache
# @login_required
def remove_apis():
    print("<<", request.form, ">>")
    data = request.form
    for d in data.getlist('apis'):
        # TODO :
        # lets find if the api is already in use or not
        # if its in use then just remove the boolean flag
        # else remove the entry from the database.
        api = ApiRequests.query.filter_by(id=d).first()
        api.flag_used = True
        db.session.flush()
    db.session.commit()
    return redirect(url_for('uploaded_file'))


@app.route('/upload_scenarios', methods=['GET', 'POST'])
@login_required
def upload_scenarios():
    if request.method == 'POST':

        if 'file' not in request.files:
            print("no file part")
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = ''.join(random.sample(string.ascii_lowercase, 10))
            filename = os.path.join(app.config['UPLOAD_FOLDER'],
                                    secure_filename(filename))
            file.save(filename)
            proj = request.form.to_dict()['projects']
            print(type(proj))
            proj = Project.query.filter_by(name=proj).first()
            print(proj)
            uploadFile(filename, proj)
            return redirect(url_for('uploaded_file'))

        return render_template('v2/dashboard.html')
    project_dict = User.get_projects(session['user_id'])
    return render_template("v2/upload.html", projects=project_dict)


@app.route('/test')
@login_required
def test():
    return render_template('v2/upload_tcs.html')


@app.route('/about')
@login_required
def about():
    return render_template('gentella/about.html')


# @app.route('/contact', methods=['GET', 'POST'])
# @login_required
# def contact():
#     form = ContactForm()

#     if request.method == 'POST':
#         if form.validate() is False:
#             flash('All fields are required.')
#             return render_template('gentella/contact.html', form=form)
#         msg = Message(form.subject.data,
#                       sender='contact@example.com',
#                       recipients=['your_email@example.com'])
#         msg.body = """
#                    From: %s <%s>
#                    %s
#                    """ % (form.name.data,
#                           form.email.data,
#                           form.message.data)
#         mail.send(msg)
#         return render_template('gentella/contact.html', success=True)
#     return render_template('gentella/contact.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm(request.form)
    form.projects.choices = [(a.id, a.name) for a in
                             Project.query.order_by('id')]
    print(form.validate())
    flash(form.errors)
    print(form.errors)
    if request.method == 'POST' and form.validate_on_submit():
        print("Inside post")
        user = User(email=form.email.data,
                    password=form.password.data,
                    projects=form.projects.data)
        print(">>> ", user)
        db.session.add(user)
        db.session.flush()
        print("---", user.id, user, "---")
        db.session.commit()
        flash('Thanks for registering')
        return redirect("/")
    print("<><>")

    return render_template('gentella/signup.html',
                           form=form)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = RegistrationForm(request.form)
#     form.projects.choices = [(a.id, a.name) for a in
#                              Project.query.order_by('id')]
#     print(form.validate())
#     flash(form.errors)
#     print(form.errors)
#     if request.method == 'POST' and form.validate_on_submit():
#         print("Inside post")
#         user = User(form.email.data, form.password.data, form.projects.data)
#         print(">>> ", user)
#         db.session.add(user)
#         db.session.flush()
#         print("---", user.id, user, "---")
#         db.session.commit()
#         flash('Thanks for registering')
#         return redirect("/")
#     print("<><>")

#     signin_form = SigninForm()
#     return render_template('gentella/login.html',
#                            signin_form=signin_form,
#                            form=form)


@app.route('/secret_page')
@login_required
def secret_page():
    return "render_template('gentella/contact.html', success=True)"


@app.route('/profile')
@login_required
def profile():

    if 'email' not in session:
        return redirect(url_for('signin'))

    user = User.query.filter_by(email=session['email']).first()

    if user is None:
        return redirect(url_for('signin'))

    return render_template('gentella/profile.html')


@app.route('/signin', methods=['POST'])
def signin():
    form = SigninForm()

    # if 'email' in session:
    #     print(session['email'])
    #     print(">>> redirecting for profile")
    #     return redirect(url_for('profile'))

    if request.method == 'POST':
        print(""" > """, form)
        if form.validate_on_submit() is False:
            print("failed to validate", form.errors)
            return redirect(url_for('login'))
        user = User.query.filter_by(email=form.email.data).first()
        if(user):
            if user.check_password(form.password.data):
                login_user(user)
                session['email'] = form.email.data
                return redirect(url_for('home'))
                # render_template('gentella/dashboard.html', user=user)


@app.route('/signout')
def signout():
    # print(user)
    logout_user()
    if 'email' not in session:

        return redirect(url_for('login'))
    session.pop(id, None)
    return redirect(url_for('home'))


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login?next=' + request.path)


@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    session['user_id'] = user_id
    return user

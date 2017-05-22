from apps import app
from flask import render_template, request, flash, session, url_for, redirect
from .forms import ContactForm, SigninForm, RegistrationForm
from flask_mail import Message, Mail
from .models import db, User, Project
from apps import login_manager
from flask_login import login_required, login_user, logout_user


mail = Mail()


@app.route('/')
@app.route("/dashboard")
@login_required
def home():
    return render_template('gentella/dashboard.html')


@app.route('/upload_scenarios', methods=['GET', 'POST'])
@login_required
def upload_scenarios():
    if request.method == 'POST':
        return render_template('gentella/dashboard.html')
    return render_template("gentella/upload.html")


@app.route('/run')
def run():
    return render_template('gentella/run.html',
                           projects=["EMP", "ESOP"],
                           username="johri_m@hcl.com",
                           testcases=[{"name": "Check the Register"},
                                      {"name": "New Test for Register"}])


@app.route('/test')
@login_required
def test():
    return render_template('gentella/db2.html')


@app.route('/about')
@login_required
def about():
    return render_template('gentella/about.html')


@app.route('/contact', methods=['GET', 'POST'])
@login_required
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() is False:
            flash('All fields are required.')
            return render_template('gentella/contact.html', form=form)
        msg = Message(form.subject.data,
                      sender='contact@example.com',
                      recipients=['your_email@example.com'])
        msg.body = """
                   From: %s <%s>
                   %s
                   """ % (form.name.data,
                          form.email.data,
                          form.message.data)
        mail.send(msg)

        return render_template('gentella/contact.html', success=True)
    return render_template('gentella/contact.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
@app.route('/signup', methods=['GET', 'POST'])
def login():
    form = RegistrationForm(request.form)
    form.projects.choices = [(a.id, a.name) for a in
                             Project.query.order_by('id')]
    print(form.validate())
    flash(form.errors)
    print(form.errors)
    if request.method == 'POST' and form.validate_on_submit():
        print("Inside post")
        user = User(form.email.data, form.password.data, form.projects.data)
        print(">>> ", user)
        db.session.add(user)
        db.session.flush()
        print("---", user.id, user, "---")
        db.session.commit()
        flash('Thanks for registering')
        return redirect("/")
    print("<><>")

    signin_form = SigninForm()
    return render_template('gentella/login.html',
                           signin_form=signin_form,
                           form=form)


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

    if 'email' in session:
        return redirect(url_for('profile'))

    if request.method == 'POST':
        print(""" > """, form)
        if form.validate_on_submit() is False:
            return render_template('gentella/login.html')
        user = User.query.filter_by(email=form.email.data).first()
        if(user):
            if user.check_password(form.password.data):
                login_user(user)
                return render_template('gentella/dashboard.html', user=user)
        # session['email'] = form.email.data
        # return redirect(url_for('profile'))

    # elif request.method == 'GET':
    #     return render_template('gentella/dashboard.html', form=form)


@app.route('/signout')
def signout():
    logout_user()
    if 'email' not in session:

        return redirect(url_for('/signin'))
    session.pop('email', None)
    return redirect(url_for('home'))


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

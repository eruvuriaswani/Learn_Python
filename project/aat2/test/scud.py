
# Login Section
from flask_login import LoginManager


# Create the login manager
login_manager = LoginManager()
# Setup the app in the login_manager
login_manager.setup_app(app)

login_manager.login_view = "login"



@login_manager.user_loader
def load_user(user):
    return Admin.query.get(user)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login and validate the user...
        login_user(form.admin)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))
    return render_template("login.html", form=form)


@app.route("/secret")
@login_required
def secret():
    return render_template('urls.html')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

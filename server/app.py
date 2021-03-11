import os
from flask import Flask, request, redirect, jsonify, flash, render_template
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension

from flask_admin import Admin
from forms import LoginForm, CreateUserForm
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from models import User, Event, MyModelView, db, connect_db

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "you should have a password in your config file")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///gulfport_votes')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True
toolbar = DebugToolbarExtension(app)

connect_db(app)

# instatiate and create admin view to edit events database table
admin = Admin(app)
admin.add_view(MyModelView(Event, db.session))
admin.add_view(MyModelView(User, db.session))

# instantiate and initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)

# connects flask-login users with database users
@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except:
        return None


@app.route('/', methods=['GET'])
def home():
    return jsonify({ "status": "Home page successfully loaded"})

@app.route('/createuser', methods=['GET', 'POST'])
def create_user():
    form = CreateUserForm()
    if form.validate_on_submit():
        try:
            user = User.create_user(form.username.data, form.password.data)

            if not user:
                raise AssertionError("Unable to insert user into database.")
            
            login_user(user)

            return redirect("/admin")
        except:
            flash("Invalid create user attempt.")
    return render_template("create_user.html", form=form)


# GET request returns login page with login
# POST request authenticates user and redirects to admin page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("You're already logged in.  You may logout or use the links on the toolbar to navigate.")
        return redirect('/admin')
    
    form = LoginForm()
    if form.validate_on_submit():
        try:
            username = form.username.data
            password = form.password.data

            user = User.is_valid(username=username, password=password)
            login_user(user)
            
            return redirect("/admin")
        except:
            flash("Invalid login attempt.")
            return redirect('/login')

    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash("You have successfully logged out.")
        return redirect('/admin')
    else:
        flash("You are not currently logged in.  To login, click the 'Login' button for further access.")
        return redirect('/admin')

@app.route("/events", methods=["GET", "POST"])
def events():
    """If POST, then add post to database, otherwise return all posts"""

    events = Event.all_events()
    return jsonify(events = events)
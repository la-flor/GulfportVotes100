import os
from flask import Flask, request, redirect, jsonify
# from flask_debugtoolbar import DebugToolbarExtension

from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from models import User, connect_db

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "you should have a password in your config file")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///gulfport_votes')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# toolbar = DebugToolbarExtension(app)

connect_db(app)

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
    if request.method == 'POST':
        try:
            user = User.create_user(request.json.get('username'), request.json.get('password'))

            if not user:
                raise AssertionError("Unable to insert user into database.")
            
            login_user(user)

            return jsonify({ "status": "New user successfully created."})
        except:
            return jsonify({ "status": "Unsuccessful create user attempt."})
    return jsonify({ "status": "Welcome to the create new user page."})


# GET request returns login page with login
# POST request authenticates user and redirects to admin page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/admin')
    if request.method == 'POST':
        try:
            username = request.json.get('username')
            password = request.json.get('password')

            user = User.is_valid(username=username, password=password)
            login_user(user)
            
            return jsonify({ "status": "Login successful"})
        except:
            return jsonify({ "status": "Unsuccessful login attempt."})

    return jsonify({ "status": "Login page successfully loaded."})

@app.route('/admin')
@login_required
def admin_page():
    return jsonify({ "status": "Admin page successfully loaded."})

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return jsonify({ "status": "Successfully logged out."})
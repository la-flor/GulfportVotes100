from flask import Flask, render_template
from flask_cors import CORS
from models import db, connect_db
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///gulfport_votes'
app.config['SECRET_KEY'] = 'Super_Secret_TO_Be_Changed'

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True
toolbar = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/events')
def events_page():
    return render_template('events.html')

@app.route('/social')
def social_page():
    return render_template('social.html')

@app.route('/voting')
def voting_page():
    return render_template('voting.html')
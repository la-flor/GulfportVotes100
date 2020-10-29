from flask import Flask, request, jsonify
from flask_cors import CORS
from admin import db, Admin, connect_db
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///gulfport_votes'
app.config['SECRET_KEY'] = 'Super_Secret_TO_Be_Changed'

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True
toolbar = DebugToolbarExtension(app)

connect_db(app)

@app.route('/admin', methods=['POST'])
def admin_login():
    username = request.form['email']
    password = request.form['password']
    
    # import pdb; pdb.set_trace()
    return jsonify({ "status": "successful" })

from flask_sqlalchemy import SQLAlchemy
import requests
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    """Connect this database to provided Flask app."""

    db.app = app
    db.init_app(app)

class Admin(db.Model):
    """Admin Users"""
    __tablename__ = "admin"

    username = db.Column(db.Text, primary_key=True)

    password = db.Column(db.String(20), nullable=False)

    @classmethod
    def authenticate(cls, username, pwd):
        """Validate admin login attempt is valid"""

        admin = Admin.query.filter_by(username=username).first()

        if admin and bcrypt.check_password_hash(admin.password, pwd):
            return admin
        else:
            return False
    
    # @classmethod
    # def add_admin(cls):
    #     """Gives current admin ability to create admin users and validate via email"""
    #     # if user is authenticated and logged in, request to add user will be sent via email


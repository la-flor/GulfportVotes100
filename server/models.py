import os
from flask_login import UserMixin
from flask import redirect
from app import db
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from flask_bcrypt import Bcrypt

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

bcrypt = Bcrypt()


class User(UserMixin, db.Model):
    """Define user"""
    __tablename__ = "users"

    id = db.Column(db.Integer,
                    primary_key=True)
    
    email = db.Column(db.VARCHAR(320),
                            unique=True,
                            nullable=False)

    password = db.Column(db.Text,
                            unique=True,
                            nullable=False)

    def get_reset_token(self, expire_time=43200000):
        # token expire_time is 12 hours
        s = Serializer(os.environ.get('SECRET_KEY'), expire_time)
        return s.dumps({'user_id': self.id}).decode('utf-8')
    
    @staticmethod
    def change_password(user, new_password):
        """Change user password"""

        hashed_pwd = bcrypt.generate_password_hash(new_password).decode('UTF-8')

        user.password = hashed_pwd
        db.session.commit()

        return user

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(os.environ.get('SECRET_KEY'))
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
    
    def __repr__(self):
        return f"User('{self.email}')"

    @classmethod
    def create_user(cls, email, password):
        """Create a new user.  Hashes password and adds user to system."""

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            email=email,
            password=hashed_pwd,
        )

        db.session.add(user)
        db.session.commit()

        return user
    
    @classmethod
    def is_valid(cls, email, password):
        """Find user with 'email' and 'password'."""

        user = cls.query.filter_by(email=email).first()
        is_authorized = bcrypt.check_password_hash(user.password, password)
        if is_authorized:
            return user
        else:
            raise AssertionError("Unable to validate user info.")



class Event(db.Model):
    """Define event"""
    __tablename__ = "events"

    id = db.Column(db.Integer,
                    primary_key=True)
    title = db.Column(db.Text,
                        nullable=False)
    description = db.Column(db.Text,
                            nullable=False)
    scheduled_time = db.Column(db.TIMESTAMP(timezone=False),
                            nullable=False)

    @staticmethod
    def all_events():
        """Retrieves and returns all events in our database."""
        
        events_query = Event.query.all()
        if not len(events_query):
            return {"events": "There are no events created."}
        else:
            events = []
            for event in events_query:
                events.append({
                    "id": event.id,
                    "title": event.title,
                    "description": event.description,
                    "scheduled_time": event.scheduled_time
                })
            return events

    @classmethod
    def create_event(cls, title, description, scheduled_time):
        """Create a event."""

        event = Event(
            title=title,
            description=description,
            scheduled_time=scheduled_time
        )

        db.session.add(event)
        db.session.commit()

        return { 
            "id": event.id, 
            "title": event.title, 
            "description": event.description, 
            "scheduled_time": event.scheduled_time 
            }

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect("/login")

    column_exclude_list = ['password']
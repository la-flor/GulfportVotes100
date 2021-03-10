from flask_login import UserMixin

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
bcrypt = Bcrypt()


class User(UserMixin, db.Model):
    """Define user"""
    __tablename__ = "users"

    id = db.Column(db.Integer,
                    primary_key=True)
    
    username = db.Column(db.Text,
                            unique=True,
                            nullable=False)

    password = db.Column(db.Text,
                            unique=True,
                            nullable=False)

    @classmethod
    def create_user(cls, username, password):
        """Create a new user.  Hashes password and adds user to system."""

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            password=hashed_pwd,
        )

        db.session.add(user)
        db.session.commit()

        return user
    
    @classmethod
    def is_valid(cls, username, password):
        """Find user with 'username' and 'password'."""

        user = cls.query.filter_by(username=username).first()
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

def connect_db(app):
    """Connect this database to provided Flask App"""

    db.app = app
    db.init_app(app)
from app import db
from models import User, Event

# Must first `createdb gulfport_votes` in CLI to create our psql database
# creates sample password = "passwords"

db.drop_all()
db.create_all()

db.session.add(User(email="testuser@gmail.com", password="$2b$12$k7bl2ufz91/HfRq86T6mQ.7jStvvzM0XwrEiv/eaddo06.YPQvuTe"))

db.session.commit()

print('DB flask_login created with sample user with an unencrypted password')
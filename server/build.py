from models import User, db

# Must first `createdb gulfport_votes` in CLI to create our psql database

db.drop_all()
db.create_all()

db.session.add(User(username="PracticeUser", password="Passwords1"))

db.session.commit()

print('DB flask_login created with sample user with an unencrypted password')
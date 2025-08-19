from flask_login import UserMixin
from app import mongo, bcrypt

class User(UserMixin):
    def __init__(self, username, password_hash, _id=None):
        self.username = username
        self.password_hash = password_hash
        self.id = str(_id) if _id else None

    @staticmethod
    def create_user(username, password):
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        user_id = mongo.db.users.insert_one({
            "username": username,
            "password": password_hash
        }).inserted_id
        return User(username, password_hash, user_id)

    @staticmethod
    def find_by_username(username):
        data = mongo.db.users.find_one({"username": username})
        if data:
            return User(data["username"], data["password"], data["_id"])
        return None

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

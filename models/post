from app import mongo
from datetime import datetime

class Post:
    @staticmethod
    def create_post(author, title, content):
        return mongo.db.posts.insert_one({
            "author": author,
            "title": title,
            "content": content,
            "created_at": datetime.utcnow()
        })

    @staticmethod
    def get_all_posts():
        return list(mongo.db.posts.find().sort("created_at", -1))

    @staticmethod
    def get_post(post_id):
        return mongo.db.posts.find_one({"_id": post_id})

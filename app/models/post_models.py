from ctypes import Union
import pymongo
from datetime import datetime as dt

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["entrega_9"]

class Post:
    def __init__(self, **kwargs):
        self.title = kwargs["title"]
        self.author = kwargs["author"]
        self.tags = kwargs["tags"]
        self.content = kwargs["content"]
        self.created_at = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        self.id = 0

    def create_post(self):
        db.post.insert_one(self.__dict__)
    

    def serialixe_post(post: any):
        if type(post) is dict:
            post.update({"_id": str(post["_id"])})
        elif type(post) is Post:
            post._id = str(post._id)
        
        return post

    @staticmethod
    def get_all():
        return db.post.find()

    @staticmethod
    def get_post_by_id(id):
        post = db.post.find({"id":id})

        return post

    @staticmethod        
    def delete_post(id):
        deleted_post = db.devs.find_one_and_delete({"id":id})

        return deleted_post
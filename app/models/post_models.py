from typing import Union
import pymongo
from datetime import datetime as dt
from pymongo import ReturnDocument

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["kenzie"]

class Post:
    def __init__(self, **kwargs):
        self.title = kwargs["title"]
        self.author = kwargs["author"]
        self.tags = kwargs["tags"]
        self.content = kwargs["content"]
        self.created_at = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        self.id = len(list(db.post.find())) + 1

    def create_post(self):
        db.post.insert_one(self.__dict__)
    

    def serialixe_post(post: Union["Post", dict]):
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
        post = list(post)
        print(post)
        return post

    @staticmethod        
    def delete_post(id):
        deleted_post = db.post.find_one_and_delete({"id":id})

        return deleted_post

    @staticmethod
    def update_post(id:str, data:dict):
        paylod = list(db.post.find({"id":id}))
        if not paylod:
            return paylod

        for item in paylod:
            item["updated_at"] = dt.now().strftime("%Y-%m-%d %H:%M:%S")
            print(item) 
        
        post = db.post.find_one_and_update(
            {"id":id}, 
            {"$set":paylod[0]}, 
            return_document=ReturnDocument.AFTER)


        post = Post.serialixe_post(post)

        return post

    @staticmethod
    def validate_keys(keys:set, data:dict):
        bory_keys_set = set(data.keys())

        return bory_keys_set - keys
        
    


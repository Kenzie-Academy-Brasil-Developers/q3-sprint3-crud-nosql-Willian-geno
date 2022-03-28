from http import HTTPStatus
from http.client import CREATED
import re


from flask import jsonify
from app.models.post_models import Post

def create_post(post:dict):
    new_post = Post(**post)
    
    new_post.create_post()

    result = Post.serialixe_post(new_post)

    return result.__dict__, HTTPStatus.CREATED

def get_post():
    post_list = Post.get_all()
    result = list(post_list)
    result = Post.serialixe_post(result)
    print(result)

    return jsonify(result) , HTTPStatus.OK 

def read_post_by_id(id):
    result = Post.get_post_by_id(id)
    if not result:
        return {"error":f'id{id}, not found'}, HTTPStatus.NOT_FOUND
    
    Post.serialixe_post(result)

    return result, HTTPStatus.OK

def delete_post(id):
    result = Post.delete_post(id)
    if not result:
        return {"error":f'id{id}, not found'}, HTTPStatus.NOT_FOUND
    
    Post.serialixe_post(result)

    return result, HTTPStatus.OK
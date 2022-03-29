from http import HTTPStatus
from http.client import CREATED
import re


from flask import jsonify, request
from app.models.post_models import Post

def create_post():
    validate_kays = {"title", "author", "tags", "content"}

    data = request.get_json()

    valid_keys = Post.validate_keys(validate_kays, data)
    print(valid_keys)
    if valid_keys :
        return {"error":"kays invalidas","expected_keys":f'{validate_kays}'}, 404

    new_post = Post(**data)
    
    new_post.create_post()

    result = Post.serialixe_post(new_post)

    return result.__dict__, HTTPStatus.CREATED

def get_post():
    post_list = Post.get_all()
    result = list(post_list)

    for post in result:
        post.update({"_id":str(post["_id"])})

    return jsonify(result) , HTTPStatus.OK 

def read_post_by_id(id):
    result = Post.get_post_by_id(id)
    if not result:
        return {"error":f'id {id}, not found'}, HTTPStatus.NOT_FOUND
    
    for post in result:
        post.update({"_id":str(post["_id"])})

    return jsonify(result), HTTPStatus.OK

def delete_post(id):
    result = Post.delete_post(id)
    if not result:
        return {"error":f'id{id}, not found'}, HTTPStatus.NOT_FOUND
    
    Post.serialixe_post(result)

    return result, HTTPStatus.OK

def update_post(id):
    validate_kays = {"title", "author", "tags", "content"}
    data = request.get_json()

    valid_keys = Post.validate_keys(validate_kays, data)

    if valid_keys :
        return {"error":"kays invalidas","expected_keys":f'{validate_kays}'}, 404

    post = Post.update_post(id, data)
    if not post:
        return {"error":f'id {id}, not found'}, HTTPStatus.NOT_FOUND

    return post, HTTPStatus.CREATED
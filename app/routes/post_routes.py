from flask import request
from app.controllers import post_controlles

def def_route(app):
    @app.get("/post")
    def get_posts():
        return post_controlles.get_post()

    @app.post('/post')
    def create_post():
        data = request.get_json()
        return post_controlles.create_post(data)

    @app.get("/posts/<int:id>")
    def read_post_by_id(id):
        return post_controlles.read_post_by_id(id)

    @app.delete("/post/<int:id>")
    def delete_post(id):
        return post_controlles.delete_post(id)


    

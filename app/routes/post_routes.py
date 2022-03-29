from flask import request
from app.controllers import post_controlles

def def_route(app):
    @app.get("/posts")
    def get_posts():
        return post_controlles.get_post()

    @app.post('/posts')
    def create_post():
        return post_controlles.create_post()

    @app.get("/posts/<int:id>")
    def read_post_by_id(id:int):
        return post_controlles.read_post_by_id(id)

    @app.patch("/posts/<int:id>")
    def update_post(id):
        return post_controlles.update_post(id)
        
    @app.delete("/posts/<int:id>")
    def delete_post(id):
        return post_controlles.delete_post(id)


    

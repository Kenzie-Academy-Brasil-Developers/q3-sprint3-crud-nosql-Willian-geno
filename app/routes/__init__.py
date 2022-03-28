from app.routes.home_route import home_roure
from app.routes.post_routes import def_route

def init_app(app):
    def_route(app)
    home_roure(app)

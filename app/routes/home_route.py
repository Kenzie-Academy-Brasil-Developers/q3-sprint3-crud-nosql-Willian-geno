def home_roure(app):
    @app.get("/")
    def home():
        return "",200

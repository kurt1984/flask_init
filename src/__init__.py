from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "hello!!"

    @app.route("/customers/")
    def customers():
        return "hello from customers!"

    @app.route("/customers/<id>")
    def customer_id(id):
        return f"hello from customer number {id}!"

    return app

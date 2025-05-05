from flask import Flask
from routes.route_users import users_router


app = Flask(__name__)


@app.get("/")
def hello_world():
    return "Hello to the main page"


app.register_blueprint(users_router)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()


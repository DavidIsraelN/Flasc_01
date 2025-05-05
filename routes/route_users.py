from flask import Blueprint

users_router = Blueprint('users', __name__, url_prefix='/users')


@users_router.route('')
def get_users():
    return "Now you need to get a list of all users"

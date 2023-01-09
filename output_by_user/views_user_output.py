from flask import render_template, Blueprint

from functions import get_posts_by_user

user_output_blueprint = Blueprint('user_output_blueprint', __name__, template_folder='templates')


@user_output_blueprint.route('/users/<username>')
def user_output(username):
    posts = get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts, username=username)

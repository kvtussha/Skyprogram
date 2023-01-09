from flask import Flask, jsonify, Blueprint, render_template
from functions import get_posts_all, get_post_by_pk

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route("/api/posts")
def posts_json():
    posts = get_posts_all()
    return jsonify(posts)

@api_blueprint.route("/api/posts/<post_id>")
def id_comments_json(post_id):
    post = get_post_by_pk(post_id)
    return jsonify(post)
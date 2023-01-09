from flask import render_template, Blueprint
from functions import comments_count, get_post_by_pk, get_comments_by_post_id

viewing_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')


@viewing_blueprint.route('/posts/<int:post_id>')
def viewing_page(post_id):
    comments = get_comments_by_post_id(post_id)
    post = get_post_by_pk(post_id)
    count_comments = comments_count(len(comments))
    return render_template("post.html", comments=comments, id=post_id, post=post, count_comments=count_comments)
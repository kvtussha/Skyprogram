from flask import Blueprint, request, render_template
from functions import search_for_posts

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


@search_blueprint.route('/')
def search_page():
    return render_template('search.html')


@search_blueprint.route('/search')
def page_search():
    search_query = request.args.get('s')
    posts = search_for_posts(search_query)
    length_posts = len(posts)
    return render_template('search.html', posts=posts, length_posts=length_posts)


import logging
from flask import Flask
from all_posts.views_all_posts import main_blueprint
from api.api_views import api_blueprint
from viewing_post.views_posts import viewing_blueprint
from search.views_search import search_blueprint
from output_by_user.views_user_output import user_output_blueprint


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(main_blueprint)
app.register_blueprint(viewing_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_output_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def error_404(e):
    return 'Страница не сущесвтует', 404


@app.errorhandler(500)
def error_500(e):
    return 'Ошибка на стороне сервера', 500


logging.basicConfig(filename="api.log", level=logging.INFO, encoding='utf-8')
logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

app.run()

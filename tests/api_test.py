import pytest
from app import app

test_keys = [
        "poster_name",
        "poster_avatar",
        "pic",
        "content",
        "views_count",
        "likes_count",
        "pk"
    ]

class TestApi:
    def test_api_posts(self):
        unusual_list = list()
        response = app.test_client().get('/api/posts').json
        for post in response:
            for key in test_keys:
                if post[key] == '':
                    unusual_list.append(key)
        assert unusual_list == [], "Ошибка"
        assert type(response) == list(), 'Ошибка'

    def test_api_post(self):
        unusual_list = list()
        response = app.test_client().get('/api/posts/<post_id>').json
        for key in test_keys:
            if key == '':
                unusual_list.append(key)
        assert unusual_list == [], "Ошибка"
        assert type(response) == dict(), 'Ошибка'



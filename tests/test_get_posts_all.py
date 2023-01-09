import pytest
from functions import get_posts_all

parameters = [
    (get_posts_all()[0]["views_count"], 376),
    (get_posts_all()[7]["poster_name"], "larry"),
]

@pytest.mark.parametrize('data, answer', parameters)
def test_get_posts_all(data, answer):
    assert type(get_posts_all() == list(), 'Неверно. Должен быть список')
    assert get_posts_all()[0]["views_count"] == answer, 'Данные получаются неверно'
import pytest
from functions import get_comments_all

parameters = [
    (get_comments_all()[1]["commenter_name"], "jlia"),
    (get_comments_all()[3]["comment"], "Интересно. А где это?"),
]

@pytest.mark.parametrize('data, answer', parameters)
def test_get_posts_all(data, answer):
    assert type(get_comments_all()) == list(), 'Неверно. Должен быть список'
    assert get_comments_all()[1]["commenter_name"] == answer, 'Данные получаются неверно'


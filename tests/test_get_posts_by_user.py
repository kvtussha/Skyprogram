import pytest
from functions import get_posts_by_user, get_posts_all

parameters = [
    ("larry", get_posts_all()[3], get_posts_all()[7]),
    ("johnny", get_posts_all()[1], get_posts_all()[5])
]

@pytest.mark.parametrize('name, text_1, text_2', parameters)
def test_get_posts_by_user(name, text_1, text_2):
    text = [text_1, text_2]
    assert get_posts_by_user(name) == text, 'По имени выводятся неправильные словари'



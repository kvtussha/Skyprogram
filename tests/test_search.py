import pytest
from functions import search_for_posts, get_posts_all

parameters = [
    ('красивый', get_posts_all()[6]),
    ('фотка', get_posts_all()[4])
]

@pytest.mark.parametrize('word, text', parameters)
def test_comments_post_id(word, text):
    assert search_for_posts(word) == text, 'Поиск по слову работает некорректно'

wrong_parameters = [
    (1, TypeError),
    (1.0, TypeError),
    ('1', TypeError),
    (-1, ValueError)
]

@pytest.mark.parametrize("str_word, exception", wrong_parameters)
def test_wrong_comments_post_id(str_word, exception):
    with pytest.raises(exception):
        search_for_posts(str_word)
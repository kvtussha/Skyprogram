import pytest
from functions import get_comments_by_post_id, get_comments_all

parameters = [
    (7, get_comments_all()[19]),
    (6, get_comments_all()[18])
]

@pytest.mark.parametrize('number, text', parameters)
def test_comments_post_id(number, text):
    assert get_comments_by_post_id(number) == text, 'Комментарии по post_id работают некорректно'

wrong_parameters = [
    (1.0, TypeError),
    ('1', TypeError),
    (-1, ValueError)
]

@pytest.mark.parametrize("int_number, exception", wrong_parameters)
def test_wrong_comments_post_id(int_number, exception):
    with pytest.raises(exception):
        get_comments_by_post_id(int_number)
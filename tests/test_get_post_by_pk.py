import pytest
from functions import get_post_by_pk, get_posts_all

parameters = [
    (1, get_posts_all()[0]),
    (5, get_posts_all()[4]),
    (8, get_posts_all()[7])
]

@pytest.mark.parametrize("number, text", parameters)
def test_comments_count(number, text):
    assert get_post_by_pk(number) == text, "Неправильный пост по pk"

wrong_parameters = [
    (1.0, TypeError),
    ('1', TypeError),
    (-1, ValueError)
]

@pytest.mark.parametrize("int_number, exception", wrong_parameters)
def test_wrong_get_post_by_pk(int_number, exception):
    with pytest.raises(exception):
        get_post_by_pk(int_number)
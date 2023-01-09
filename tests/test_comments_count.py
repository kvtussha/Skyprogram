from functions import comments_count
import pytest

comments = [
    (1, "1 комментарий"),
    (4, "4 комментария"),
    (5, "5 комментариев"),
    (9, "9 комментариев"),
    (0, "0 комментариев"),
    (126, "126 комментариев")
]

@pytest.mark.parametrize("number, text", comments)
def test_comments_count(number, text):
    assert comments_count(number) == text, "Комментарии склоняются неправильно"

wrong_comments = [
    (1.0, TypeError),
    ('1', TypeError),
    (-1, ValueError)
]

@pytest.mark.parametrize("int_number, exception", wrong_comments)
def test_wrong_comments_count(int_number, exception):
    with pytest.raises(exception):
        comments_count(int_number)


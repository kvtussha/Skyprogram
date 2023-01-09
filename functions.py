import json
import pprint
import os


def get_posts_all() -> list[dict[str, int | str]]:
    """Загрузка постов из json"""
    with open(os.path.join('data', 'posts.json'), 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def get_posts_by_user(user_name) -> list:
    """Возвращает посты определенного пользователя"""
    posts = get_posts_all()
    posts_list = []
    post_name = []
    for post in posts:
        if user_name == post["poster_name"]:
            posts_list.append(post)
            post_name.append(post["poster_name"])
            if post["content"] == "":
                return []
    return posts_list


def get_comments_all():
    """Загрузка комментариев из json"""
    with open(os.path.join('data', 'comments.json'), 'r', encoding='utf-8') as file:
        comments = json.load(file)
    return comments


def get_comments_by_post_id(post_id) -> list:
    """Возвращает комментарии определенного поста. """
    comments = get_comments_all()
    comments_list = []
    post_id_list = set()
    for comment in comments:
        if comment["post_id"] == post_id:
            comments_list.append(comment)
            post_id_list.add(post_id)
    if post_id not in post_id_list:
        raise ValueError('Такого поста нет')
    return comments_list


def comments_count(comments_count: int) -> str:
    if type(comments_count) != int: raise TypeError('Должно быть целое число')
    if comments_count < 0: raise ValueError('Должно быть не меньше 0')
    """Функция для использования правильных окончаний"""
    reminder = comments_count % 10
    if 5 <= reminder <= 9 or reminder == 0:
        return f"{comments_count} комментариев"
    if reminder == 1:
        return f"{comments_count} комментарий"
    if 2 <= reminder <= 4:
        return f"{comments_count} комментария"


def search_for_posts(query) -> list[dict[str, str | int]]:
    """Возвращает список постов по ключевому слову"""
    posts = get_posts_all()
    posts_query = []
    for post in posts:
        if query in post["content"]:
            posts_query.append(post)
    return posts_query


def get_post_by_pk(pk) -> dict[str, str | int]:
    """Возвращает один пост по его идентификатору. """
    posts = get_posts_all()
    for post in posts:
        if post["pk"] == pk:
            return post

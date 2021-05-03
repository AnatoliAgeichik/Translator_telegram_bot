import pytest
from app.connect_db import add_new_user, get_all_users, delete_user, get_language_from, get_language_target, \
                            update_language_target_for_user, update_language_from_for_user

test_user_id = 125


@pytest.fixture(autouse=True)
def create_user():
    add_new_user(test_user_id)
    yield
    delete_user(test_user_id)


def test_add_new_user_without_lang():
    assert test_user_id in get_all_users()


def test_add_new_user_with_lang():
    test_user_id = 123
    delete_user(test_user_id)
    lang_target = "fr"
    lang_from = "en"
    add_new_user(test_user_id, lang_target, lang_from)
    assert test_user_id in get_all_users() and lang_target == get_language_target(test_user_id) and \
           lang_from == get_language_from(test_user_id)


def test_add_user_with_lang_target():
    test_user_id = 123
    delete_user(test_user_id)
    lang_target = "be"
    add_new_user(test_user_id, lang_target)
    assert test_user_id in get_all_users() and lang_target == get_language_target(test_user_id)
    delete_user(test_user_id)


def test_change_target_language():
    target_lang = "fr"
    update_language_target_for_user(test_user_id, target_lang)
    assert target_lang == get_language_target(test_user_id)


def test_change_from_language():
    lang_from = "fr"
    update_language_from_for_user(test_user_id, lang_from)
    assert lang_from == get_language_from(test_user_id)

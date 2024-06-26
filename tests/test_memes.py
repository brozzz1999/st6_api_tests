import pytest
from data_payloads import testdata, payload_create_meme as payl_cr, payload_name, payload_urls
from data_payloads import bad_token, none_meme_id


def test_create_meme(token, create_meme):
    headers = {"Authorization": token}
    create_meme.create_new_meme(payl_cr, headers)
    create_meme.check_response_is_200()
    create_meme.check_meme_text(payl_cr['text'])
    create_meme.check_meme_url(payl_cr['url'])
    create_meme.check_meme_info(payl_cr['info'])


@pytest.mark.parametrize("text, url, tags, info", payload_urls, ids=["int", "None", "invalid"])
def test_create_meme_bad_url(token, create_meme, text, url, tags, info):
    headers = {"Authorization": token}
    create_meme.create_new_meme(payload_urls, headers)
    create_meme.check_response_is_400()


def test_delete_meme(delete_meme, meme_id, token):
    delete_meme.delete(meme_id, token)
    delete_meme.check_response_is_200()


def test_delete_meme_bad_token(delete_meme, meme_id):
    delete_meme.delete(meme_id, bad_token)
    delete_meme.check_response_is_401()


def test_delete_none_meme(delete_meme, token):
    delete_meme.delete(none_meme_id, token)
    delete_meme.check_response_is_404()


def test_get_meme(get_meme, meme_id, token):
    get_meme.get_new_meme(meme_id, token)
    get_meme.check_response_is_200()


def test_get_meme_bad_token(get_meme, meme_id):
    get_meme.get_new_meme(meme_id, bad_token)
    get_meme.check_response_is_401()


def test_get_all_memes(get_meme, token):
    get_meme.get_all_memes(token)
    get_meme.check_response_is_200()


@pytest.mark.parametrize("text, url, info", testdata, ids=["one", "two", "three"])
def test_update_meme(update_meme, token, meme_id, text, url, info):
    payload = {
        "id": meme_id,
        "text": text,
        "url": url,
        "tags": ["ha-ha-ha", "humor"],
        "info": info
    }
    update_meme.update_meme(token, meme_id, payload)
    update_meme.check_response_is_200()
    update_meme.check_meme_text(text)
    update_meme.check_meme_url(url)
    update_meme.check_meme_info(info)


@pytest.mark.parametrize("text, url, tags, info", payload_name, ids=["int", "None", "much"])
def test_create_memes_bad_name(token, create_meme, text, url, tags, info):
    headers = {"Authorization": token}
    create_meme.create_new_meme(payload_name, headers)
    create_meme.check_response_is_400()

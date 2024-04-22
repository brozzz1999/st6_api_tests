import allure
import pytest
import requests
from endpoints.create_meme import CreateMeme
from endpoints.delete_meme import DeleteMeme
# from endpoints.get_meme import GetMeme
# from endpoints.update_meme import UpdateMeme
# from endpoints.patch_meme import PatchMeme



# @pytest.mark.parametrize('token', token)
def test_create_meme(token, create_meme):
    headers = {"Authorization": token}
    payload = {
        "text": "Piu-pau oy oy oy",
        "url": "https://imgflip.com/i/8ngjno",
        "tags": ["piu", "pi-piu"],
        "info": {"rating": 1, "fun": 2}
    }
    create_meme.create_new_meme(payload, headers)
    create_meme.check_response_is_200()
    # create_meme.check_response_url_is_()


def test_delete_meme(meme_id, delete_meme, token):
    delete_meme.delete(meme_id, token)
    delete_meme.check_response_is_200()

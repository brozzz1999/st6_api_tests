import pytest
import requests
from endpoints.create_meme import CreateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.get_meme import GetMeme
from endpoints.update_meme import UpdateMeme

PAYLOAD = {"name": "vkuklin"}


@pytest.fixture()
def start():
    print('\nStart testing')
    yield


@pytest.fixture()
def token(payload=PAYLOAD):
    response = requests.post('http://167.172.172.115:52355/authorize', json=payload)
    token = response.json()['token']
    yield token


@pytest.fixture()
def create_meme():
    return CreateMeme()


@pytest.fixture()
def meme_id(create_meme, token):
    headers = {"Authorization": token}
    payload = {
        "text": "Piu-pau oy oy oy",
        "url": "https://imgflip.com/i/8ngjno",
        "tags": ["piu", "pi-piu"],
        "info": {"rating": 1, "fun": 2}
    }
    create_meme.create_new_meme(payload, headers)
    meme_id = create_meme.response_json['id']
    yield meme_id
    DeleteMeme().delete(meme_id, token)


@pytest.fixture()
def get_meme():
    return GetMeme()


@pytest.fixture()
def update_meme():
    return UpdateMeme()


@pytest.fixture()
def delete_meme():
    return DeleteMeme()

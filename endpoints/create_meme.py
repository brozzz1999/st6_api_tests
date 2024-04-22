import requests
import allure
from endpoints.base_endpoint import BaseEndpoint


@allure.suite('Create new meme')
class CreateMeme(BaseEndpoint):
    @allure.step('Send meme request')
    def create_new_meme(self, payload, headers):
        # headers = headers if headers else HEADERS
        # payload = payload if payload else PAYLOAD
        self.response = requests.post('http://167.172.172.115:52355/meme', json=payload, headers=headers)
        self.status_code = self.response.status_code
        self.response_json = self.response.json()
        # self.url_meme = self.response_json()['url']
        # self.meme_id = self.response.json()['id']

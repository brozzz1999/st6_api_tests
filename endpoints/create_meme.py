import requests
import allure
from endpoints.base_endpoint import BaseEndpoint


@allure.suite('Create new meme')
class CreateMeme(BaseEndpoint):
    @allure.step('Send meme request')
    def create_new_meme(self, payload, headers):
        self.response = requests.post('http://167.172.172.115:52355/meme', json=payload, headers=headers)
        self.status_code = self.response.status_code
        if self.status_code == 200:
            self.response_json = self.response.json()

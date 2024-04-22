import requests
import allure
from endpoints.base_endpoint import BaseEndpoint

token = None

PAYLOAD = {"name": "vkuklin"}


@allure.suite('Create token')
class CreateMeme(BaseEndpoint):
    @allure.step('Send username request')
    def create_token(self, payload=PAYLOAD):
        self.response = requests.post('http://167.172.172.115:52355/authorize', json=payload)
        self.response_json = self.response.json()
        self.token = self.response_json['token']

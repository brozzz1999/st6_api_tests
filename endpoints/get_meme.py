import requests
import allure
from endpoints.base_endpoint import BaseEndpoint


@allure.suite('Getting meme')
class GetMeme(BaseEndpoint):
    @allure.step('Get meme request')
    def get_new_meme(self, meme_id, token):
        headers = {"Authorization": token}
        self.response = requests.get(f'http://167.172.172.115:52355/meme/{meme_id}', headers=headers)
        self.status_code = self.response.status_code
        self.response_json = self.response.json()
        # self.url_meme = self.response_json()['url']
        # self.meme_id = self.response.json()['id']

    @allure.step('Get all memes request')
    def get_all_memes(self, token):
        headers = {"Authorization": token}
        self.response = requests.get('http://167.172.172.115:52355/meme', headers=headers)
        self.status_code = self.response.status_code
        self.response_json = self.response.json()

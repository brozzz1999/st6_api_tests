import requests
import allure

from endpoints.base_endpoint import BaseEndpoint

meme_id = None
PAYLOAD = None


class UpdateMeme(BaseEndpoint):

    @allure.step('Update meme request')
    def update_meme(self, token, meme_id, payload=None):
        headers = {"Authorization": token}
        payload = payload if payload else PAYLOAD
        self.response = requests.put(f'http://167.172.172.115:52355/meme/{meme_id}', json=payload, headers=headers)
        self.status_code = self.response.status_code

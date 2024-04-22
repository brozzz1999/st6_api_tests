import requests
import allure
from endpoints.base_endpoint import BaseEndpoint
from endpoints.create_meme import CreateMeme


class DeleteMeme(BaseEndpoint):

    @allure.step('Delete meme')
    def delete(self, meme_id, token):
        headers = {"Authorization": token}
        self.response = requests.delete(f'http://167.172.172.115:52355/meme/{meme_id}', headers=headers)
        self.status_code = self.response.status_code

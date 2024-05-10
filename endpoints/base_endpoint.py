import allure


class BaseEndpoint:
    response = None
    status_code = None
    response_json = None
    payload = None
    token = None
    HEADERS = {"Authorization": token}

    @allure.step('Check status code 200')
    def check_response_is_200(self):
        assert self.status_code == 200

    @allure.step('Check status code 400')
    def check_response_is_400(self):
        assert self.status_code == 400

    @allure.step('Check status Unauthorized 401')
    def check_response_is_401(self):
        assert self.status_code == 401

    @allure.step('Check status 404 Not Found')
    def check_response_is_404(self):
        assert self.status_code == 404

    @allure.step('Check text')
    def check_meme_text(self, text):
        assert self.response.json()['text'] == text

    @allure.step('Check url')
    def check_meme_url(self, url):
        assert self.response.json()['url'] == url

    @allure.step('Check info')
    def check_meme_info(self, info):
        assert self.response.json()['info'] == info

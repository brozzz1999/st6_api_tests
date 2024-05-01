from locust import task, HttpUser


class MemeUser(HttpUser):
    meme_ids = set()
    token = None

    def on_start(self):
        response = self.client.post('/authorize', json={'name': 'vkuklin'}).json()
        self.token = response['token']

    @task(7)
    def get_all_memes(self):
        self.client.get('/meme', headers={'Authorization': self.token})

    @task(1)
    def create_meme(self):
        payload = {
            "text": "Piu-pau oy oy oy",
            "url": "https://imgflip.com/i/8ngjno",
            "tags": ["piu", "pi-piu"],
            "info": {"rating": 1, "fun": 2}
        }
        response = self.client.post('/meme', json=payload, headers={'Authorization': self.token}).json()
        self.meme_ids.add(response['id'])

    def on_stop(self):
        for meme_id in self.meme_ids:
            self.client.delete(f'/meme/{meme_id}', headers={'Authorization': self.token})

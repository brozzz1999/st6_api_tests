testdata = [
    ('1', 'http://google.com', {"rating": 555, "fun": 11}),
    ('Text 2', 'http://ya.com', {"rating": 111, "fun": 22}),
    ('Text 3' * 5, 'http://mail.ru', {"rating": 333, "fun": 33})
]

payload_create_meme = {
        "text": "Piu-pau oy oy oy",
        "url": "https://imgflip.com/i/8ngjno",
        "tags": ["piu", "pi-piu"],
        "info": {"rating": 1, "fun": 2}
    }

payload_name = [
    (30, 'http://google.com', ["piu", "pi-piu"], {"rating": 555, "fun": 11}),
    (None, 'http://ya.com', ["piu", "pi-piu"], {"rating": 111, "fun": 22}),
    ('Text' * 99, 'http://mail.ru',["piu", "pi-piu"], {"rating": 333, "fun": 33})
]

payload_urls = [
    ("TEXT1", 1, ["piu", "pi-piu"], {"rating": 555, "fun": 11}),
    ("TEXT2", '', ["piu", "pi-piu"], {"rating": 111, "fun": 22}),
    ('TEXT3', 'http://mail.ru@ru.ru.ru',["piu", "pi-piu"], {"rating": 333, "fun": 33})
]

bad_token = '0000'
none_meme_id = 00000

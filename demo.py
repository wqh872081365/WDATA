# -*- coding: utf-8 -*-

import requests
proxies = {
    "https": "https://172.16.21.63:1080"
}
response_index = requests.get("https://www.youtube.com/", proxies=proxies)
print len(response_index.text)
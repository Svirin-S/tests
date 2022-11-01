from wsgiref import headers
import requests

TOKEN = ''
URL = 'https://cloud-api.yandex.net/v1/disk/resources'


def upload(path_to_file, token):
    upload_url = URL
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                'Authorization': f'OAuth {token}'}
    params = {'path': path_to_file, 'overwrite': 'true'}
    res = requests.put(upload_url, headers=headers, params=params)
    return res.status_code 

print(upload('Music33', TOKEN))    
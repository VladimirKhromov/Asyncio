import requests

def get_status(url: str) -> int:
    responce = requests.get(url)
    return responce.status_code

url = 'https://www.example.com'
print(get_status(url))
print(get_status(url))

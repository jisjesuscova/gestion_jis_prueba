import requests

url = 'https://apijis.azurewebsites.net/login_users/token'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'grant_type': '',
    'username': '27141399',
    'password': '123456',
    'scope': '',
    'client_id': '',
    'client_secret': ''
}

response = requests.post(url, headers=headers, data=data)
print(response.json())
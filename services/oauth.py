import base64

from http_utils import HttpStatus

CLIENT_ID = ''
CLIENT_SECRET = '' 

def check_token():
    pass

def get_token(username, password, client):
    print('1')
    response = client.post("/services/auth/token", json={
        "username": username,
        "password": password
    }, headers={
        'Accept': 'application/json', 
        'Authorization': base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'),
        'Content-Type': 'application/json'
    })
    print('2')

    if response.status_code == HttpStatus.OK:
        return response.json()
    else:
        print(response.status_code)
        raise Exception("Unauthorized")
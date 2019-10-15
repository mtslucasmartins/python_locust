import json
import requests

from models import VirtualUser

DOMAIN = 'https://development-api-comunicacao.herokuapp.com'

APPLICATION_JSON = 'application/json'

def authorize(vu: VirtualUser):
    url = '{}/services/auth/token'.format(DOMAIN)

    headers = {'Content-Type': APPLICATION_JSON, 'Accept': APPLICATION_JSON}
    body = {'email': vu.email, 'password': vu.password}

    print('----- ----- ----\n')
    print('URL ........: {}'.format(url))
    print('Headers ....: {}'.format(headers))
    print('Body .......: {}'.format(body))
    print('\n----- ----- ----\n\n')
        
    authorize_response = requests.post(url, json=body, headers=headers)

    if authorize_response.status_code == 200:
        authorize_json_response = authorize_response.json()
    
        record = authorize_json_response.get('record')

        vu.access_token = record.get('token')
        vu.details = record.get('user')

        return vu

def request_01():
    pass


def request_02():
    pass


def request_03():
    pass


def run(vu: VirtualUser):
    vu = authorize(vu)

    print(vu.access_token)
    print(vu.details)
# 
import json 
from models import VirtualUser
from script import authorize as vu_authorize

max_requests = 100
num_requests = 0

virtual_users = []

def read_vu_file(filepath='./vu.json'):
    with open(filepath) as json_file:  
        data = json.load(json_file)
        for p in data['vu']:
            username = p['email']
            password = p['password']

            print('\n\n')
            print('Email .....: ' + username)
            print('Password ..: ' + password)
            print('')

            vu = vu_authorize(VirtualUser(
                email=username,
                password=password
            ))

            print('Token .....: ' + vu.access_token)
            virtual_users.append(vu)

def run():
    read_vu_file()
    
    for vu in virtual_users:
        print(vu.access_token)


if __name__ == "__main__":
    
    run()
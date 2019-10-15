import base64

from locust import HttpLocust, TaskSet, task
from credentials import USER_CREDENTIALS

import services.oauth as oauth_service

from http_utils import HttpStatus

BETA = 'https://beta-ottimizza-oauth-server.herokuapp.com'
DEV = 'https://development-oauth-server.herokuapp.com'

DOMAIN = BETA
    
CLIENT_ID = 'bussola-contabil-client'
CLIENT_SECRET = 'bussola-contabil-secret' 

class WebsiteTasks(TaskSet):

    def __init__(self, parent):
        super(WebsiteTasks, self).__init__(parent)
        self.host = DOMAIN
        self.auth_session = {}
        self.basic_headers = {}
        self.username = ""
        self.password = ""

        self.access_token = ""
        self.user_details = {}
        self.headers = {}

    def on_start(self):
        print('WebsiteTasks.on_start')

        if len(USER_CREDENTIALS) > 0:
            self.username, self.password = USER_CREDENTIALS.pop()

            print(self.username)
            print(self.password)

            try:
                self.basic_headers = {
                    'Authorization': 'Basic ' + base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()).decode(),
                }

                response = self.client.post("/oauth/token?grant_type=password", {
                    "username": self.username,
                    "password": self.password
                }, headers=self.basic_headers)
                if response.status_code == 200:
                    self.auth_session = response.json()

                else:
                    print(response.json())
                    self.interrupt()

            except Exception as ex:
                print('Hell No')
                print(ex)
                # self.interrupt()


            # if authorize_response.status_code == HttpStatus.OK:
            #     authorize_json_response = authorize_response.json()

            #     status = authorize_json_response.get('status', 'error')

            #     if status == 'success':
            #         record = authorize_json_response.get('record')

            #         self.access_token = record.get('token')
            #         self.user_details = record.get('user')

            #         self.headers = {'Authorization': 'Bearer ' + self.access_token, 'Content-Type': 'application/json'}
            #     else:
            #         print("""\n
            #             Email: {}
            #             Password: {}
            #         """.format(self.email, self.password))
            #         self.interrupt()
            # else:   
            #     print("""\n
            #         Email: {}
            #         Password: {}
            #     """.format(self.email, self.password))
            #     

    @task # "/services/contacts/{}/contacts"
    def get_contacts(self):
        if self.auth_session.get('access_token') is not None:
            url = f"/oauth/check_token?token={self.auth_session.get('access_token')}"
            response = self.client.get(url, headers=self.basic_headers)


class WebsiteUser(HttpLocust):
    host = DOMAIN
    task_set = WebsiteTasks
    min_wait = 1000
    max_wait = 1100

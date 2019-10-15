class VirtualUser:

    def __init__(self, *args, **kwargs):
        self.email = kwargs.get('email', None)
        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)
        self.__details = kwargs.get('details', {})
        self.__access_token = kwargs.get('access_token', '')

    @property
    def details(self):
        return self.__details

    @details.setter
    def details(self, details):
        self.__details = details

    @property
    def access_token(self):
        return self.__access_token

    @access_token.setter
    def access_token(self, access_token):
        self.__access_token = access_token

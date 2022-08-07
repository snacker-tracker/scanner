import requests
import os
import datetime
import time


class TokenProvider:
    def __init__(self, TENANT, CLIENT_ID, CLIENT_SECRET, **options):
        self._cached_token = None
        self.provider = "".join([
            options.get('procotol', "https://"),
            TENANT
        ])
        self.credentials = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET
        }

        print(self.credentials)

        self.options = options

    def get_token(self):
        if type(self._cached_token) is not dict:
            self._cached_token = self._request_token()

        if time.mktime(datetime.datetime.now().timetuple()) >= self._cached_token_expiry:
            self._cached_token = self._request_token()

        return self._cached_token['access_token']

    def _request_token(self):
        response = requests.post(
            self.provider + "/oauth/token",
            data = {
                "client_id": self.credentials['client_id'],
                "client_secret": self.credentials['client_secret'],
                "grant_type": "client_credentials",
                "audience": self.options.get('audience')
            }
        )

        token = response.json()

        self._cached_token_expiry = time.mktime(datetime.datetime.now().timetuple()) + (token['expires_in'] - token['expires_in']/10)

        return token

    token = property(get_token)

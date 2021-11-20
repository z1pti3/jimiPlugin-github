import requests
import json
import time
from pathlib import Path

class _github():
    url = "https://api.github.com"

    def __init__(self, ca=None, requestTimeout=30):
        self.requestTimeout = requestTimeout
        if ca:
            self.ca = Path(ca)
        else:
            self.ca = None

    def apiCall(self,endpoint,methord="GET",data=None):
        kwargs={}
        kwargs["timeout"] = self.requestTimeout
        if self.ca:
            kwargs["verify"] = self.ca
        try:
            url = "{0}/{1}".format(self.url,endpoint)
            if methord == "GET":
                response = requests.get(url, **kwargs)
            elif methord == "POST":
                kwargs["data"] = data
                response = requests.post(url, **kwargs)
            elif methord == "DELETE":
                response = requests.delete(url, **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            return 0, "Connection Timeout"
        if response.status_code == 200 or response.status_code == 202:
            return json.loads(response.text)
        return None

    def getRateLimit(self):
        response = self.apiCall("rate_limit")
        return response

    def getLatestCommits(self,owner,repo):
        response = self.apiCall("repos/{0}/{1}/commits".format(owner,repo))
        return response

    def getLatestCommit(self,owner,repo):
        response = self.apiCall("repos/{0}/{1}/commits".format(owner,repo))
        return response[0]


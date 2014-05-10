import json


class MockConnector(object):
    def __init__(self, token, uri, version):
        self.response = None
        self.status_code = None
        self.token = token
        self.uri = uri
        self.version = version

    def set_response(self, response, status_code):
        self.response = MockResponse(response, status_code)

    def post(self, body, resource, params={}, extra_headers={}):
        return self.response

    def get(self, body, resource, extra_headers={}):
        return self.response


class MockResponse(object):
    def __init__(self, response, status_code):
        self.response = response
        self.status_code = status_code

    def json(self):
        return self.response

    @property
    def text(self):
        return json.dumps(self.response)

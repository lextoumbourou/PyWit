import requests
import urllib


class Connector(object):
    def __init__(self, token, uri):
        self.token = token
        self.uri = uri

    def _request(self, req_method, body, resource, extra_headers):
        """Return the JSON response if successful, otherwise return None"""

        headers = {'Authorization': 'Bearer {0}'.format(self.token)}
        headers = dict(headers.items() + extra_headers.items())
        url = "{0}/{1}".format(self.uri, resource)

        return req_method(url, data=body, headers=headers)

    def get(self, body, resource, url_params={}, extra_headers={}):
        resource = resource + urllib.urlencode(url_params)
        return self._request(
            requests.get, body, resource, extra_headers)

    def post(self, body, resource, url_params={}, extra_headers={}):
        resource = resource + urllib.urlencode(url_params)
        return self._request(
            requests.post, body, resource, extra_headers)

    def delete(self, body, resource, url_params={}, extra_headers={}):
        resource = resource + urllib.urlencode(url_params)
        return self._request(
            requests.delete, body, resource, extra_headers)

    def put(self, body, resource, url_params={}, extra_headers={}):
        resource = resource + urllib.urlencode(url_params)
        return self._request(
            requests.put, body, resource, extra_headers)

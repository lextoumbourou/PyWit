import requests
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


class Connector(object):
    def __init__(self, token, uri, version):
        self.token = token
        self.uri = uri
        self.version = version

    def _get_versioned_params(self, url_params):
        if 'v' not in url_params:
            url_params['v'] = self.version
        return urlencode(url_params)

    def _request(self, req_method, body, resource, url_params, extra_headers):
        """Return the JSON response if successful, otherwise return None"""

        headers = {'Authorization': 'Bearer {0}'.format(self.token)}
        headers.update(**extra_headers)
        resource = '{0}?{1}'.format(
            resource, self._get_versioned_params(url_params))
        url = "{0}/{1}".format(self.uri, resource)

        return req_method(url, data=body, headers=headers)

    def get(self, body, resource, url_params={}, extra_headers={}):
        if body:
            url_params.update(body)

        return self._request(
            requests.get, {}, resource, url_params, extra_headers)

    def post(self, body, resource, url_params={}, extra_headers={}):
        return self._request(
            requests.post, body, resource, url_params, extra_headers)

    def delete(self, body, resource, url_params={}, extra_headers={}):
        return self._request(
            requests.delete, body, resource, url_params, extra_headers)

    def put(self, body, resource, url_params={}, extra_headers={}):
        return self._request(
            requests.put, body, resource, url_params, extra_headers)

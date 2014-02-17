import json

from connector import Connector
from exception import (
    AuthenticationFailedError, ResourceNotFoundError,
    BadRequestError, ContentTypeNotSupportedError)


class Wit(object):
    """Wit object handles communication with wit.ai using their HTTP API"""

    SUPPORTED_CONTENT = ['wav', 'mpeg3', 'ulaw']

    def __init__(self, token, connector=Connector):
        self.uri = 'https://api.wit.ai'
        self.token = token
        self._connector = connector(token, self.uri)
        self.last_response = None

    def _is_valid_content_type(self, content_type):
        return content_type in self.SUPPORTED_CONTENT

    def _handle_response(self, response):
        self.last_response = response

        if response.status_code in (200, 201):
            return response.json()
        elif response.status_code == 401:
            raise AuthenticationFailedError(response.text)
        elif response.status_code == 404:
            raise ResourceNotFoundError(response.text)
        else:
            raise BadRequestError(response.text)

    def get_message(self, q, context=None, meta=None, msg_id=None):
        body = {'q': q}
        if context:
            body['context'] = context
        if meta:
            body['meta'] = meta
        if msg_id:
            body['msg_id'] = msg_id

        response = self._connector.get(body, 'message')
        return self._handle_response(response)

    def post_speech(self, file_obj=None, content_type='',
                    context=None, meta=None, msg_id=None):
        """Return JSON from a posted sound file

        :param file_obj: A file object (needs to have the read() method)
        :param content_type: A string presenting the file type (eg wav, mpeg)
        :param context: Context object (see https://wit.ai/docs/api)
        :param meta: Additional request info (see https://wit.ai/docs/api)
        :param msg_id: A specific message id (see https://wit.ai/docs/api)
        """

        file_data = file_obj.read()

        if not self._is_valid_content_type(content_type):
            raise ContentTypeNotSupportedError

        params = {}
        if context:
            params['context'] = context
        if meta:
            params['meta'] = meta
        if msg_id:
            params['msg_id'] = msg_id

        headers = {'Content-Type': 'audio/{0}'.format(content_type)}

        response = self._connector.post(file_data, 'speech', params, headers)
        return self._handle_response(response)

    def get_message_by_id(self, message_id):
        response = self._connector.get({}, 'messages/{0}'.format(message_id))
        return self._handle_response(response)

    def get_intents(self):
        response = self._connector.get({}, 'intents')
        return self._handle_response(response)

    def get_corpus(self):
        headers = {'Accept': 'application/json'}
        response = self._connector.get({}, 'corpus', extra_headers=headers)
        return self._handle_response(response)

    def get_entities(self):
        response = self._connector.get({}, 'entities')
        return self._handle_response(response)

    def get_entities_by_id(self, entity_id):
        response = self._connector.get({}, 'entities/{0}'.format(entity_id))
        return self._handle_response(response)

    def post_entities(self, entity_id, doc=None, values=None):
        body = {'id': entity_id}
        if doc:
            body['doc'] = doc
        if values:
            body['values'] = values

        response = self._connector.post(
            json.dumps(body), 'entities',
            extra_headers={'Content-Type': 'application/json'})
        return self._handle_response(response)

    def update_entity(self, entity_id, doc=None, values=None):
        body = {}
        if doc:
            body['doc'] = doc
        if values:
            body['values'] = values

        response = self._connector.put(
            json.dumps(body), 'entities/{0}'.format(entity_id), {'Content-Type': 'application/json'})
        return self._handle_response(response)

    def delete_entity(self, entity_id):
        response = self._connector.delete({}, 'entities/{0}'.format(entity_id))
        return self._handle_response(response)

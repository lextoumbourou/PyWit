import json

from connector import Connector
from exceptions import (
    AuthenticationFailedError, ResourceNotFoundError,
    BadRequestError, ContentTypeNotSupportedError)


class Wit(object):
    """Wit object exposes methods for communicating with Wit's HTTP API"""

    SUPPORTED_CONTENT = ['wav', 'mpeg3', 'ulaw']

    def __init__(self, token, connector=Connector, raw_text=False):
        self.uri = 'https://api.wit.ai'
        self.token = token
        self._connector = connector(token, self.uri)
        self.last_response = None
        self.raw_text = raw_text

    def _is_valid_content_type(self, content_type):
        return content_type in self.SUPPORTED_CONTENT

    def _handle_response(self, response):
        self.last_response = response

        if response.status_code in (200, 201):
            if self.raw_text:
                return response.text
            else:
                return response.json()
        elif response.status_code == 401:
            raise AuthenticationFailedError(response.text)
        elif response.status_code == 404:
            raise ResourceNotFoundError(response.text)
        else:
            raise BadRequestError(response.text)

    def get_message(self, query, context=None, meta=None, msg_id=None):
        """Return extracted meaning from a sentence

        :param query: User's query. Length is > 0 and < 256 chars
        :param context: (optional) user's context
        :param meta: (optional) Additional request info
        :param msg_id: (optional) A specific message id

        Refer to https://wit.ai/docs/api#toc_3
        """

        body = {'q': query}
        if context:
            body['context'] = context
        if meta:
            body['meta'] = meta
        if msg_id:
            body['msg_id'] = msg_id

        response = self._connector.get(body, 'message')
        return self._handle_response(response)

    def post_speech(self, data=None, content_type='wav',
                    context=None, meta=None, msg_id=None):
        """Return meaning extracted from a posted sound file

        :param data: A file-like object, bytes array or iterator
                     Anything that can be passed as the data arg
                     to the ``requests.post`` method can be passed here

                     See http://requests.readthedocs.org/en/latest/api/
        :param content_type: A string presenting the file type (eg wav, mpeg3)
                             Assumes wav by default
        :param context: (optional) user's context
        :param meta: (optional) Additional request info
        :param msg_id: (optional) A specific message id

        Refer to https://wit.ai/docs/api#toc_8
        """
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

        response = self._connector.post(data, 'speech', params, headers)
        return self._handle_response(response)

    def get_message_by_id(self, message_id):
        """Return a stored message for an id

        :param message_id: message id

        Refer to https://wit.ai/docs/api#toc_13
        """
        response = self._connector.get({}, 'messages/{0}'.format(message_id))
        return self._handle_response(response)

    def get_intents(self):
        """Return a list of intents (without their expressions)

        Refer to https://wit.ai/docs/api#toc_15
        """
        response = self._connector.get({}, 'intents')
        return self._handle_response(response)

    def get_corpus(self):
        """Return a list of validated expressions in your instance

        Refer to https://wit.ai/docs/api#toc_17
        """
        headers = {'Accept': 'application/json'}
        response = self._connector.get({}, 'corpus', extra_headers=headers)
        return self._handle_response(response)

    def get_entities(self):
        """Return a list of entities for the instance

        Refer to https://wit.ai/docs/api#toc_18
        """
        response = self._connector.get({}, 'entities')
        return self._handle_response(response)

    def get_entity_by_id(self, entity_id):
        """Return an entity from an id

        :param entity_id: ID of requested entity

        Refer to https://wit.ai/docs/api#toc_20
        """
        response = self._connector.get({}, 'entities/{0}'.format(entity_id))
        return self._handle_response(response)

    def post_entity(self, entity_id, doc=None, values=None):
        """Create a new entity

        :param entity_id: ID of entity
        :param doc: (optional) short sentence describing the entity
        :param values: (optional) possible values for entity

        Refer to https://wit.ai/docs/api#toc_22
        """
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
        """Update an entity with attributes

        :param entity_id: ID of entity
        :param doc: (optional) short sentence describing the entity
        :param values: (optional) possible values for entity

        Refer to https://wit.ai/docs/api#toc_25
        """
        body = {}
        if doc:
            body['doc'] = doc
        if values:
            body['values'] = values

        response = self._connector.put(
            json.dumps(body), 'entities/{0}'.format(entity_id), {},
            extra_headers={'Content-Type': 'application/json'})
        return self._handle_response(response)

    def delete_entity(self, entity_id):
        """Permanently remove an entity

        :param entity_id: ID of entity

        Refer to https://wit.ai/docs/api#toc_28
        """
        response = self._connector.delete(
            {}, 'entities/{0}'.format(entity_id),
            extra_headers={'Content-Type': 'application/json'})
        return self._handle_response(response)

    def get_entities_by_id(self, *args, **kwargs):
        """Alias for get_entity_by_id"""
        return self.get_entity_by_id(*args, **kwargs)

    def put_entities(self, *args, **kwargs):
        """Alias for update_entity"""
        return self.update_entity(*args, **kwargs)

    def delete_entities(self, *args, **kwargs):
        """Alias for delete_entity"""
        return self.delete_entity(*args, **kwargs)

    def post_entities(self, *args, **kwargs):
        """Alias for post_entity"""
        return self.post_entity(*args, **kwargs)

import sys
from connector import Connector

class ContentTypeNotSupportedError(Exception):
    pass

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

    def get_message(self, q, context=None, meta=None, msg_id=None):
        body = {'q': q}
        if context:
            body['context'] = context
        if meta:
            body['meta'] = meta
        if msg_id:
            body['msg_id'] = msg_id

        result = self._connector.get(body, 'message')
        self.last_response = result
        if result.status_code == 200:
            return result.json()

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

        headers = {'Content-Type': 'audio/{0}'.format(content_type)}

        result = self._connector.post(file_data, 'speech', headers)
        self.last_response = result
        if result.status_code == 200:
            return result.json()

    def get_message_by_id(self, message_id):
        result = self._connector.get({}, 'messages/{0}'.format(message_id))
        self.last_response = result
        if result.status_code == 200:
            return result.json()

    def get_intents(self):
        return self._connector.get(body, 'intents')

    def get_corpus(self):
        return self._connector.get(body, 'corpus')

    def get_entities(self):
        return self._connector.get(body, 'entities')

    def get_entities_by_id(self, entity_id):
        return self._connector.get(body, 'entities/{0}'.format(entity_id))

    def post_entity(self, entity_id, doc=None, values=None):
        data = {'id': entity_id}
        if doc:
            data['doc'] = doc
        if values:
            data['values'] = values

        return self._connector.put(data, 'entities', {'Content-Type': 'application/json'})

    def update_entity(self, entity_id, doc=None, values=None):
        data = {'id': entity_id}
        if doc:
            data['doc'] = doc
        if values:
            data['values'] = values

        return self._connector.put(data, 'entities', {'Content-Type': 'application/json'})

    def delete_entity(self, entity_id):
        return self._connector.delete({}, 'entities/{0}'.format(entity_id))

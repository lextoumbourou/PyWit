import os
import unittest
from getpass import getpass

import wit


class TestWitOnline(unittest.TestCase):
    def setUp(self):
        try:
            self.token = os.environ['WIT_ACCESS_TOKEN']
        except KeyError:
            print('WIT Access token not set, skipping test')
            self.token = None

        self.wit = wit.Wit(self.token)

    def test_message(self):
        if self.token:
            results = self.wit.get_message('Hello')
            assert type(results) == dict
        else:
            assert False

    def test_message_accepts_context_and_meta_as_dict(self):
        if self.token:
            context = {'timezone': 'Australia/Melbourne'}
            meta = {'source': 'Something'}
            results = self.wit.get_message('Hello', context, meta)
            assert type(results) == dict
            assert results['msg_body'] == 'Hello'
        else:
            assert False

    def test_speech_from_file(self):
        if self.token:
            context = {'timezone': 'Australia/Melbourne'}
            meta = {'source': 'Something'}
            file_obj = open(
                os.path.dirname(os.path.abspath(__file__)) +
                '/../data/hello_world.wav', 'rb')
            results = self.wit.post_speech(
                file_obj, content_type='wav',
                context=context, meta=meta)
            assert results['msg_body'] == 'hello world'
        else:
            assert False

    def test_raw_speech_from_file(self):
        if self.token:
            file_obj = open(
                os.path.dirname(os.path.abspath(__file__)) +
                '/../data/hello_world.raw', 'rb')
            content_type = \
                'raw;encoding=signed-integer;bits=16;rate=44100;endian=little'
            results = self.wit.post_speech(
                file_obj, content_type=content_type)
            assert results['msg_body'] == 'hello world'
        else:
            assert False

    def test_get_corpus(self):
        if self.token:
            result = self.wit.get_corpus()
            assert type(result) == list
        else:
            assert False

    def test_get_entities(self):
        if self.token:
            result = self.wit.get_entities()
            assert type(result) == list
        else:
            assert False

    def test_get_entities_by_id(self):
        if self.token:
            ents = self.wit.get_entities()
            result = self.wit.get_entities_by_id(ents[0])
            assert type(result) == dict
        else:
            assert False


if __name__ == "__main__":
    if 'WIT_ACCESS_TOKEN' not in os.environ:
        os.environ['WIT_ACCESS_TOKEN'] = getpass('Enter Wit Access Token: ')
        unittest.main()

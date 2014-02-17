import os
import unittest
from getpass import getpass

import wit


class IntegrationTest(unittest.TestCase):
    def setUp(self):
        self.wit = wit.Wit(os.environ['WIT_ACCESS_TOKEN'])

    def test_message(self):
        results = self.wit.get_message('Hello')
        self.assertTrue(type(results) == dict)

    def test_speech_from_file(self):
        file_obj = open('tests/data/hello_world.wav')
        results = self.wit.post_speech(file_obj, content_type='wav')
        self.assertEquals(results['msg_body'], 'hello world')

    def test_get_corpus(self):
        result = self.wit.get_corpus()
        self.assertEquals(type(result), list)

    def test_get_entities(self):
        result = self.wit.get_entities()
        self.assertEquals(type(result), list)

    def test_get_entities_by_id(self):
        ents = self.wit.get_entities()
        result = self.wit.get_entities_by_id(ents[0])
        self.assertEquals(type(result), dict)

if __name__ == "__main__":
    if 'WIT_ACCESS_TOKEN' not in os.environ:
        os.environ['WIT_ACCESS_TOKEN'] = getpass('Enter Wit Access Token: ')
        unittest.main()

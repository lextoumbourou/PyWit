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

if __name__ == "__main__":
    if 'WIT_ACCESS_TOKEN' not in os.environ:
        os.environ['WIT_ACCESS_TOKEN'] = getpass('Enter Wit Access Token: ')
        unittest.main()

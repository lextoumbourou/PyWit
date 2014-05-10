import unittest
import os

from nose.tools import raises

import mock_objects as mocks
import wit


class TestWitOffline(unittest.TestCase):
    def setUp(self):
        self.token = 'fake-token'
        self.uri = 'fake-uri'
        self.wit = wit.Wit(self.token, mocks.MockConnector)

    def test_get_message(self):
        query = 'test'
        expected = {'msg_body': query, 'msg_id': 'some-id', 'outcome': {}}
        self.wit._connector.set_response(expected, 200)
        result = self.wit.get_message(query)
        assert type(result) == dict
        assert result['msg_body'] == query

    def test_get_message_outputs_text_when_set(self):
        query = 'test'
        expected = {'msg_body': query, 'msg_id': 'some-id', 'outcome': {}}
        self.wit._connector.set_response(expected, 200)
        self.wit.raw_text = True
        result = self.wit.get_message(query)
        assert type(result) == str

    @raises(wit.AuthenticationFailedError)
    def test_get_message_raises_exception_on_auth_failure(self):
        query = 'test'
        expected = {'msg_body': query, 'msg_id': 'some-id', 'outcome': {}}
        self.wit._connector.set_response(expected, 401)
        self.wit.get_message(query)

    def test_speech_from_file(self):
        query = 'hello world'
        file_obj = open(
            os.path.dirname(os.path.abspath(__file__)) +
            '/../data/hello_world.wav')
        expected = {'msg_body': query, 'msg_id': 'some-id', 'outcome': {}}
        self.wit._connector.set_response(expected, 200)
        result = self.wit.post_speech(file_obj, content_type='wav')
        assert result['msg_body'] == 'hello world'

    def test_get_message_by_id(self):
        msg_id = 'some-id'
        expected = {'msg_body': 'hello', 'msg_id': 'some-id', 'outcome': {}}
        self.wit._connector.set_response(expected, 200)
        result = self.wit.get_message_by_id(msg_id)
        assert result['msg_id'] == msg_id

    def test_get_intents(self):
        msg_id = 'some-id'
        expected = {'msg_body': 'hello', 'msg_id': 'some-id', 'outcome': {}}
        self.wit._connector.set_response(expected, 200)
        result = self.wit.get_message_by_id(msg_id)
        assert result['msg_id'] == msg_id

    def test_get_corpus(self):
        expected = ['one', 'two', 'three']
        self.wit._connector.set_response(expected, 200)
        result = self.wit.get_corpus()
        assert len(result) == 3

    def test_get_entities(self):
        expected = ['one', 'two', 'three']
        self.wit._connector.set_response(expected, 200)
        result = self.wit.get_entities()
        assert len(result) == 3

    def test_post_entity(self):
        e_id = 'something'
        doc = 'A test'
        self.wit._connector.set_response({
            'doc': doc, 'id': e_id}, 201)
        result = self.wit.post_entity(e_id, doc=doc)
        assert 'id' in result
        assert result['doc'] == doc

    def test_update_entity(self):
        e_id = 'something'
        doc = 'New val'
        self.wit._connector.set_response({
            'doc': doc, 'id': e_id}, 200)
        result = self.wit.post_entity(e_id, doc=doc)
        assert 'id' in result
        assert result['doc'] == doc

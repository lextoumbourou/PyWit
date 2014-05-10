import unittest
import urllib

import wit

class ConnectorTest(unittest.TestCase):
    def setUp(self):
        self.token = 'ABC123'
        self.version = '20140510'
        self.uri = 'https://localhost'

    def test_can_load_class(self):
        connector = wit.Connector(self.token, self.uri, self.version)
        assert isinstance(connector, wit.Connector)

    def test_does_append_variable(self):
        connector = wit.Connector(self.token, self.uri, self.version)
        params = connector._get_versioned_params({})
        assert params == 'v={}'.format(self.version)



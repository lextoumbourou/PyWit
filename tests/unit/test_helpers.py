from wit import helpers


class TestWitHelpers(object):
    def test_process_content_type_appends_audio(self):
        content_type = 'wav'
        assert helpers.process_content_type(content_type) == 'audio/wav'
        content_type = (
            'audio/raw;encoding=unsigned-integer;bits=16;rate=8000;endian=big')
        assert helpers.process_content_type(content_type) == content_type

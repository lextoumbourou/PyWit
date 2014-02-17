# pywit

*A Python wrapper around the [Wit](http://wit.ai) HTTP API*

## Status

Alpha (first release coming very soon)

## Basic Usage

```
>>> from wit import Wit
>>> w = Wit(YOUR_TOKEN_GOES_HERE')
>>> w.get_message('Hello world')
{u'msg_body': u'Hello world', u'msg_id': u'ac7aa079-4621-499b-b54a-4378886b6330', u'outcome': {u'entities': {}, u'confidence': 0.525, u'intent': u'order'}}
>>> w.post_speech(open('tests/data/hello_world.wav'), 'wav')
{u'msg_body': u'hello world', u'msg_id': u'6a410cda-32e0-4602-bcfb-c20f5e1aed66', u'outcome': {u'entities': {}, u'confidence': 0.525, u'intent': u'order'}}
```

## Docs

Coming soon


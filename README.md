# PyWit

*Python bindings for the [Wit](http://wit.ai) HTTP API*

## Usage

```
>>> from wit import Wit
>>> w = Wit('YOUR_TOKEN_GOES_HERE')
>>> w.get_message('It puts the lotion in the basket')
{u'msg_body': u'It puts the lotion in the basket',
 u'msg_id': u'67771674-25ad-40af-b3fe-f2806c9a092a',
 u'outcome': {u'confidence': 0.525, u'entities': {}, u'intent': u'order'}}
>>> w.post_speech(open('hello_world.wav'))
{u'msg_body': u'hello world',
 u'msg_id': u'6a410cda-32e0-4602-bcfb-c20f5e1aed66',
 u'outcome': {u'entities': {}, u'confidence': 0.525, u'intent': u'order'}}
```

Read the [docs](http://pywit.readthedocs.org/en/latest/) for more.

## License

MIT

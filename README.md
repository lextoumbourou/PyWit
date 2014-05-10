# PyWit

[![Build Status](https://travis-ci.org/lextoumbourou/PyWit.png?branch=master)](https://travis-ci.org/lextoumbourou/PyWit)

*Python bindings for the [Wit](http://wit.ai) HTTP API*

## Basic Usage

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

## Documentation

Read the docs [here](http://pywit.readthedocs.org/en/latest/)

## Tests

### Unit (Offline)

```
> python -m unittest discover
```

Or via nose:

```
> nosetests
```

### Integration (Online)

```
> export WIT_ACCESS_TOKEN=YOUR_TOKEN_GOES_HERE
> python -m unittest test.integration.manual_test_wit
```

## License

MIT

## Changelog

* 0.2.0
  * Added support for Wit's versioning system
* 0.1.5
  * Added support for raw audio
  * Provided additional streamed audio example 
* 0.1.4
  * Initial PyPi-ready release

## Contributors

If you contributed to the project, feel free to add your name and/or Github username here.

* Lex Toumbourou (@lextoumbourou) - origin author
* Josh Deare (@doodles526)

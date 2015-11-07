# PyWit (Unofficial)

[![Build Status](https://travis-ci.org/lextoumbourou/PyWit.png?branch=master)](https://travis-ci.org/lextoumbourou/PyWit)
[![License](https://pypip.in/license/PyWit/badge.png)](https://pypi.python.org/pypi/PyWit)
[![Latest Version](https://pypip.in/version/PyWit/badge.png)](https://pypi.python.org/pypi/PyWit)
[![Downloads](https://pypip.in/download/PyWit/badge.png)](https://pypi.python.org/pypi/PyWit)

*Note: Wit.ai now provides an official Python SDK also called [pywit](https://github.com/wit-ai/pywit). It is the recommended way to develop Wit applications in Python.*

*Python bindings for the [Wit](http://wit.ai) HTTP API*

## Basic Usage

```python
>>> from wit import Wit
>>> w = Wit('YOUR_TOKEN_GOES_HERE')
>>> w.get_message('It puts the lotion in the basket')
{u'msg_body': u'It puts the lotion in the basket',
 u'msg_id': u'67771674-25ad-40af-b3fe-f2806c9a092a',
 u'outcome': {u'confidence': 0.525, u'entities': {}, u'intent': u'order'}}
>>> fh = open('hello_world.wav', 'rb')
>>> w.post_speech(fh)
{u'msg_body': u'hello world',
 u'msg_id': u'6a410cda-32e0-4602-bcfb-c20f5e1aed66',
 u'outcome': {u'entities': {}, u'confidence': 0.525, u'intent': u'order'}}
```

## Documentation

Read the docs [here](http://pywit.readthedocs.org/en/latest/)

## Tests

### Unit (Offline)

```bash
> nosetests tests/unit
```
### Integration (Online)

```bash
> export WIT_ACCESS_TOKEN=YOUR_TOKEN_GOES_HERE
> nosetests tests/integration
```

## Python version support

* Python 2.7 and higher (Python 2.6 should work with argparse installed: ```pip install argparse```)
* Python 3

## License

MIT

## Changelog

* 0.3.0
	* Added Python3 support
* 0.2.0
  * Added support for Wit's versioning system
  * Improved tests
* 0.1.5
  * Added support for raw audio
  * Provided additional streamed audio example 
* 0.1.4
  * Initial PyPi-ready release

## Contributors

If you contributed to the project, feel free to add your name and/or Github username here.

* Lex Toumbourou (@lextoumbourou) - origin author
* Josh Deare (@doodles526)

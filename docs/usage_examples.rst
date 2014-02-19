Usage Examples
==============

We'll need to start by initialising Wit using the token you'll find under **Settings**:

::

    >>> from wit import Wit
    >>> w = Wit('YOUR_TOKEN_WILL_GO_HERE')

Now, how about we return an extracted meaning from a sentence, based on instance data?:

::

    >>> w.get_message('It puts the lotion in the basket')
    {u'msg_body': u'It puts the lotion in the basket',
     u'msg_id': u'67771674-25ad-40af-b3fe-f2806c9a092a',
     u'outcome': {u'confidence': 0.525, u'entities': {}, u'intent': u'order'}}

PyWit will output JSON data by default when there's a response from Wit's servers. (Feature coming soon) if you want raw text, you can set that as follows:

::

    >>> w.dont_parse_json(True)

Or turn it off:

::

    >>> w.dont_parse_json(False)

Anyway, where were we? Oh yeah, you can send a Wav file up for processing by passing a file handle to the ``post_speech``` method. Like this:

::

    >>> sound = open('hello_world.wav')
    {u'msg_body': u'hello world',
     u'msg_id': u'6a410cda-32e0-4602-bcfb-c20f5e1aed66',
     u'outcome': {u'entities': {}, u'confidence': 0.525, u'intent': u'order'}}

Wit also supports mpeg3 and ulaw files. You'll need to tell PyWit what the filetype is, in that case:

::

    >>> sound = open('hello_world.mp3', file_type='mpeg3')

(Feature coming soon) You'll find a couple more examples of cool stuff to try in the **examples** directory.

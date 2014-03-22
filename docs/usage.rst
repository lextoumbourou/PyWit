Usage
=====

We start by initialising Wit using the token you'll find under your Wit account `Settings <https://console.wit.ai/#/settings>`_.

::

    >>> from wit import Wit
    >>> w = Wit('YOUR_TOKEN_WILL_GO_HERE')

To return an extracted meaning from a sentence, we use the ``get_message`` method...

::

    >>> w.get_message('It puts the lotion in the basket')
    {u'msg_body': u'It puts the lotion in the basket',
     u'msg_id': u'67771674-25ad-40af-b3fe-f2806c9a092a',
     u'outcome': {u'confidence': 0.525, u'entities': {}, u'intent': u'order'}}

...which is a simple wrapper around the `GET /message <https://wit.ai/docs/api#toc_3>`_ API call.

You can send a sound file up for meaning extraction processing by passing a file-like object to the ``post_speech`` method. Like this:

::

    >>> sound = open('hello_world.wav')
    >>> w.post_speech(sound)
    {u'msg_body': u'hello world',
     u'msg_id': u'6a410cda-32e0-4602-bcfb-c20f5e1aed66',
     u'outcome': {u'entities': {}, u'confidence': 0.525, u'intent': u'order'}}

Wit supports wav, mpeg3 and ulaw files. You'll need to tell PyWit what the filetype is if it's not a wav file.

::

    >>> sound = open('hello_world.mp3')
    >>> w.post_speech(sound, content_type='mpeg3')

See the `POST /speech <https://wit.ai/docs/api#toc_8>`_ API docs for more info.

PyWit will output JSON data by default when there's a response from Wit's servers. If you want raw text, you can set that as follows:

::

    >>> w.raw_text = True

You'll find a couple more examples of cool stuff to try in the `examples <https://github.com/lextoumbourou/PyWit/tree/master/examples>`_ directory.

Most of the other Wit API calls have been implemented in PyWit, refer to the :doc:`API Guide <api>` for examples.

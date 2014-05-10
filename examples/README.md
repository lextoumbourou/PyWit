Examples
========

To run the examples, you should have the ```WIT_ACCESS_TOKEN``` env variable set, if not, you'll be prompted for the token.

## user_input_example.py

Simply reads text from prompt and send to Wit.ai for processing.

```
> python user_input_example.py 
What should I send up? Hello, cuz
{u'msg_body': u'Hello, cuz',
 u'msg_id': u'344041ac-6cc3-48bb-b3c4-5ec498d4250b',
 u'outcome': {u'confidence': 0.545, u'entities': {}, u'intent': u'greeting'}}
```

## wav_input_example.py

Sends a wav up to Wit.ai for processing. The wav should be passed as a command line arg. It will use the local hello_world.wav file if no argument is specified.

```
> python wav_input_example.py ./hello_world.wav 
{u'msg_body': u'hello world',
 u'msg_id': u'9d8997dc-d509-49a8-8e54-d65a10f12692',
 u'outcome': {u'confidence': 0.545, u'entities': {}, u'intent': u'greeting'}}
```

## recorded_input_example.py

You will need:

* A microphone
* [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/) 

This demo is a little more complex than the other examples. It reads data in from your microphone for 3 seconds, writes it to a StringIO buffer, which is then sent straight up to Wit.ai.

```
> python recorded_input_example.py
* recording
* done recording
{u'msg_body': u'hello world',
 u'msg_id': u'9d8997dc-d509-49a8-8e54-d65a10f12692',
 u'outcome': {u'confidence': 0.545, u'entities': {}, u'intent': u'greeting'}}
```

## recorded_stream_input_example.py

Same dependencies as ```recorded_input_example.py```

The purpose of this example is to show how to stream raw audio straight from the microphone to Wit's servers.

We take in audio from the microphone using the generator called ```record_and_stream``` which is passed in as the first argument to ```Wit.post_speech```.

You might need to tweak the ```CONTENT_TYPE``` variable to match your OS's settings. It has been tested on OSX (Mountain Lion).

```
> python recorded_stream_input_example.py
* recording
* done recording
{u'msg_body': u'hello world',
 u'msg_id': u'b080bad5-41b6-4cf2-b188-db50a88bfaf8',
 u'outcome': {u'confidence': 0.515, u'entities': {}, u'intent': u'greeting'}}
```

Examples
========

To run the examples, you should have the ```WIT_ACCESS_TOKEN``` env variable set, if not, you'll be prompted for the token.

## User Input Example ```user_input_example.py```

Simply reads text from prompt and send to Wit.ai for processing.

```
> python user_input_example.py 
What should I send up? Hello, cuz
{u'msg_body': u'Hello, cuz',
 u'msg_id': u'344041ac-6cc3-48bb-b3c4-5ec498d4250b',
 u'outcome': {u'confidence': 0.545, u'entities': {}, u'intent': u'greeting'}}
```

## Wav Input Example ```wav_input_example.py```

Sends a wav up to Wit.ai for processing. The wav should be passed as a command-line arg. Feel free to use my voice:

```
> python wav_input_example.py ./hello_world.wav 
{u'msg_body': u'hello world',
 u'msg_id': u'9d8997dc-d509-49a8-8e54-d65a10f12692',
 u'outcome': {u'confidence': 0.545, u'entities': {}, u'intent': u'order'}}
```

## Recorded Input Example ```recorded_input_example.py```

You will need:

* A microphone
* [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/) 

This demo is a little more complex than the other examples. It reads data in from your microphone for 5 seconds, then writes it to a StringIO buffer, which is then sent up to Wit.Ai as chunk-encoded data.

```
> python recorded_input_example.py
```

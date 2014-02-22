import sys
import os
from pprint import pprint
from getpass import getpass
from StringIO import StringIO
import wave

try:
    import pyaudio
except ImportError:
    print('Error: Make sure you install PyAudio before running this example.')

try:
    import wit
except ImportError:
    # Wit isn't installed, so we'll add the parent directory to the system
    # path and try again
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.append(path)
    import wit

# Demo below is taken from the Record demo at PyAudio's website.
# The only variation is that we're writing to a string buffer

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 3

if __name__ == '__main__':
    output_file = StringIO()
    if 'WIT_ACCESS_TOKEN' not in os.environ:
        os.environ['WIT_ACCESS_TOKEN'] = getpass('Enter Wit Access Token: ')
    wit_token = os.environ['WIT_ACCESS_TOKEN']

    p = pyaudio.PyAudio()

    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE,
        input=True, frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(output_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    w = wit.Wit(wit_token)
    result = w.post_speech(output_file)
    pprint(result)

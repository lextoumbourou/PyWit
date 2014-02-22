import sys
import os
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
    path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
    sys.path.append(path)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
OUTPUT = StringIO()

def read_write(pyaudio_handle):
    print("* recording")
    frames = []
    wf = wave.open(OUTPUT, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        wf.writeframes(data)
        yield wf.read()
    wf.close()

if __name__ == "__main__":
    if 'WIT_ACCESS_TOKEN' not in os.environ:
        os.environ['WIT_ACCESS_TOKEN'] = getpass('Enter Wit Access Token: ')

    w = wit.Wit(os.environ['WIT_ACCESS_TOKEN'])
    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE,
        input=True, frames_per_buffer=CHUNK)
    w.post_speech(read_write(stream))

import os
import sys
from pprint import pprint

try:
    import wit
except ImportError:
    path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
    sys.path.append(path)
    import wit

if __name__ == '__main__':
    if 'WIT_ACCESS_TOKEN' not in os.environ:
        os.environ['WIT_ACCESS_TOKEN'] = getpass('Enter Wit Access Token: ')
    wit_token = os.environ['WIT_ACCESS_TOKEN']

    if len(sys.argv) < 2:
        print('No file specified, using the default')
        path = 'hello_world.wav'
    else:
        path = sys.argv[1]

    fh = open(path)

    w = wit.Wit(wit_token)
    pprint(w.post_speech(fh))

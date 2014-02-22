import os
import sys
from pprint import pprint
from getpass import getpass

try:
    import wit
except ImportError:
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.append(path)
    import wit

if __name__ == '__main__':
    if 'WIT_ACCESS_TOKEN' not in os.environ:
        os.environ['WIT_ACCESS_TOKEN'] = getpass('Enter Wit Access Token: ')
    wit_token = os.environ['WIT_ACCESS_TOKEN']
    w = wit.Wit(wit_token)
    input_text = raw_input('What should I send up? ')
    pprint(w.get_message(input_text))

import argparse
import sys
import requests
import base64
from requests.auth import HTTPBasicAuth

def call_rest(args, unknown):
    url = args['address']
    user, password = '', ''
    
    r = None

    if args.get('user'):
        user, password = args['user'].split(':')
        r = requests.get(url, auth=HTTPBasicAuth(user, password))
    else:
        r = requests.get(url)

    # can also manually encode Auth headers, but not very clean
    # b64_credentials = base64.b64encode(args['user'].encode()).decode()
    # r = requests.get(url, headers = { 'Authorization' : f'Basic {b64_credentials}'} )
    
    r_code = r.status_code
    r_json = r.json()

    if r_code == 401:
        print('Unauthorized user')
        print('Please check that you provided the right credentials')
        print(f'The server returned the message: {r_json["message"]}')
    elif r_code == 200:
        print(f'Success: {r_json["message"]}')
        print(f'The secret is {r_json["secret"]}')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', help='user:password for authorization', default='')
    parser.add_argument('address', help='REST API server url')
    parser.add_argument('-G', '--get', help='whether to make a get request', action='store_true')
    args, unknown = parser.parse_known_args()
    return vars(args), unknown

if __name__ == "__main__":

    args, unknown = parse_args()

    call_rest(args, unknown)
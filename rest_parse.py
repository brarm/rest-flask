import argparse
import sys
import requests
import base64
from requests.auth import HTTPBasicAuth
from urllib.parse import urlparse, parse_qs

def call_rest2(args, unknown):
    url = args.url
    verb = args.verb
    auth = None
    user, password = '',''
    if args.user:
        user, password = args.user.split(':')
        auth = HTTPBasicAuth(user, password)

    resp = None
    if verb == 'GET':
        resp = requests.get(url, data={}, auth=auth)
    if verb == 'POST':
        resp = requests.post(url, data={}, auth=auth)
    if verb == 'PATCH':
        pass
    if verb == 'PUT':
        pass
    if verb == 'DELETE':
        pass

    if args.include:
        print(f'\n>Request headers    : {resp.request.headers}')
        print(f'>Request URL        : {resp.request.url}')
        print(f'>Request body       : {resp.request.body}')

    print(f'\nResponse status     : {resp.status_code}')
    print('Response content    : ', end='')
    
    if resp.headers['Content-Type'] == 'application/json':
        print(resp.json())
    elif 'text' in resp.headers['Content-Type']:
        print(resp.text)

    if args.include:
        print(f'\n<Response headers   : {resp.headers}')
        

def parse_args2():
    choices = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE']
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'verb', 
        choices=choices,
        help='{GET|POST|PATCH|PUT|DELETE}',
        default='GET',
        metavar='VERB')
    parser.add_argument('url', help='REST call URL')
    parser.add_argument(
        '-u', '--user', 
        help='user:password for authorization', metavar='')
    parser.add_argument(
        '-i', '--include', 
        action='store_true', 
        dest='include',
        help='Prints header information for req/resp')
    args, unknown = parser.parse_known_args()
    return args, unknown

if __name__ == "__main__":

    args, unknown = parse_args2()

    call_rest2(args, unknown)

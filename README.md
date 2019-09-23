# A Prototype API Endpoint Communicator

Requires:
- python >= 3.4

pip packages
- flask
- requests

On Debian systems (Ubuntu, etc):
```
sudo apt-get update
sudo apt install python3

python3 -V

sudo apt install python3-pip

pip3 install -U flask requests
```

Another option is to use pyenv, which can be installed using `setup.sh`
This script targets Ubuntu and installs all the dependencies for building python from source
The setup takes some time, but pyenv is an excellent tool for managing python environments

### RUN

Create an instance of the REST server with
`python3 app.py`

In another terminal, use 
`python3 rest_parse.py`

### USAGE
```
$: python3 rest_parse.py -h
usage: rest_parse.py [-h] [-u] [-i] VERB url

positional arguments:
  VERB           {GET|POST|PATCH|PUT|DELETE}
  url            REST call URL

optional arguments:
  -h, --help     show this help message and exit
  -u , --user    user:password for authorization
  -i, --include  Prints header information for req/resp
```

### TEST

```
$: python3 rest_parse.py GET http://localhost:5000

Response status     : 200
Response content    : Welcome to the Flask Server!

$: python3 rest_parse.py POST http://localhost:5000/

Response status     : 405
Response content    : <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>

$: python3 rest_parse.py GET http://localhost:5000/echo

Response status 	: 200
Response content	: ECHO: GET

$: python3 rest_parse.py GET http://localhost:5000/nopage

Response status 	: 404
Response content	: {'message': 'Not Found: http://localhost:5000/nopage', 'status': 404}

$: python3 rest_parse.py GET http://localhost:5000/secrets

Response status 	: 401
Response content	: {'message': 'Authentication failed', 'user': None}

$: python3 rest_parse.py GET http://localhost:5000/secrets -u admin:secret

Response status 	: 200
Response content	: {'message': 'Authentication presented succesfully'}

$: python3 rest_parse.py GET http://localhost:5000/secrets -u admin:secret -i

>Request headers    : {'User-Agent': 'python-requests/2.18.4', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Basic YWRtaW46c2VjcmV0'}
>Request URL        : http://localhost:5000/secrets
>Request body       : None

Response status     : 200
Response content    : {'message': 'Authentication presented succesfully'}

<Response headers   : {'Content-Type': 'application/json', 'Content-Length': '51', 'Server': 'Werkzeug/0.16.0 Python/3.7.3', 'Date': 'Mon, 23 Sep 2019 07:30:41 GMT'}
```

### MANUAL TESTS

```
$: curl http://localhost:5000
"Welcome to the Flask Server!"

$: curl -X POST http://localhost:5000/secrets
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>

$: curl http://localhost:5000/echo
ECHO: GET

$: curl http://localhost:5000/nopage
{"message":"Not Found: http://localhost:5000/nopage","status":404}

$: curl http://localhost:5000/secrets
{"message":"Authentication failed","user":null}

$: curl http://localhost:5000/secrets -u admin:secret
{"message":"Authentication presented succesfully"}
```




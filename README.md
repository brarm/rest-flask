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

### TEST

Input: ```
python3 rest_parse.py http://localhost:5000/secrets```

Output: ```
Unauthorized user
Please check that you provided the right credentials
The server returned the message: No Authorization Headers were detected```

Input: ```
python3 rest_parse.py -u not_admin:secret http://localhost:5000/secrets```

Output: ```
Unauthorized user
Please check that you provided the right credentials
The server returned the message: The user 'not_admin' is not authorized```

Input: ```
python3 rest_parse.py -u admin:secret http://localhost:5000/secrets```

Output: ```
Success: The user 'admin' has been authorized
The secret is c2VjcmV0```


### MANUAL TESTS

```
$: curl http://localhost:5000
"Welcome to Flask Server"

$: curl http://localhost:5000/secrets
{"message": "No Authorization Headers were detected"}

$: curl -u "not_admin:secret" http://localhost:5000/secrets
{"message": "The user 'not_admin' is not authorized"}

$: curl -u "admin:secret" http://localhost:5000/secrets
{"message": "The user 'admin' has been authorized", "secret": "c2VjcmV0"}
```




# A Prototype API Endpoint Communicator

Requires:
- python >= 3.7

pip packages
- flask
- requests

Using pyenv for python is recommended
```
curl https://pyenv.run | bash

pyenv install 3.7.4
pyenv local 3.7.4

pyenv virtualenv rest-flask
pyenv activate rest-flask

pip install flask
pip install requests
```

### RUN

Create an instance of the REST server with
`python app.py`

In another terminal, use 
`python rest_parse.py`

### TEST

Input: ```
python rest_parse.py http://localhost:5000/secrets```

Output: ```
Unauthorized user
Please check that you provided the right credentials
The server returned the message: No Authorization Headers were detected```

Input: ```
python rest_parse.py -u not_admin:secret http://localhost:5000/secrets```

Output: ```
Unauthorized user
Please check that you provided the right credentials
The server returned the message: The user 'not_admin' is not authorized```

Input: ```
python rest_parse.py -u admin:secret http://localhost:5000/secrets```

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




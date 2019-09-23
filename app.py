from flask import Flask, url_for
from flask import request
from flask import Response
from flask import jsonify
from functools import wraps
import json
import base64

app = Flask(__name__)

@app.route('/')
def api_root():
    return jsonify('Welcome to the Flask Server!')

@app.route('/hello', methods = ['GET'])
def api_hello():
    data = {
        'hello' : 'world',
        'number'    : 3
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://localhost'

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status' : 404,
        'message': 'Not Found: ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    
    return resp

@app.route('/users/<userid>', methods = ['GET'])
def api_users(user_id):
    users = {'1':'john', '2':'steve', '3':'bill'}
    if userid in users:
        return jsonify({userid:users[userid]})
    else:
        return not_found()

@app.route('/echo', methods= ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PATCH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"

@app.route('/messages', methods = ['POST'])
def api_message():
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data
    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)
    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return 'Binary message written!'
    else:
        return '415 Unsupported Media Type'


def check_auth(username, password):
    return username =='admin' and password == 'secret'

def authenticate(user=None):
    
    message = {
        'message'   : 'Authentication failed',
        'user'      :  user
        }
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'

    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return authenticate()
        elif not check_auth(auth.username, auth.password):
            return authenticate(auth.username)
        print(*args)
        print(**kwargs)
        return f(*args, **kwargs)

    print(decorated)
    return decorated


@app.route('/secrets', methods=['GET'])
@requires_auth
def secrets():
    print(request.headers)
    message = {'message' : 'Authentication presented succesfully'}
    return jsonify(message)

if __name__ == '__main__':
    app.run()

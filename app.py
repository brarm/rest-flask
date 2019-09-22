from flask import Flask, url_for
from flask import request
from flask import Response
import json
import base64

app = Flask(__name__)

@app.route('/')
def api_root():
	return json.dumps('Welcome to Flask Server')

@app.route('/secrets', methods=['GET'])
def secrets():
	resp = Response()
	data = {}
	if not (request.headers.get('Authorization')):
		print('no auth headers')
		data = { 'message': 'No Authorization Headers were detected'}
		resp.status_code = 401

	else:
		base64_credentials = request.headers.get('Authorization').split(' ')[1]
		str_credentials = base64.b64decode(base64_credentials).decode('ascii')
		username, password = str_credentials.split(':')
		
		if username == 'admin':
			data = {
				' message'	: 'The admin user has been authorized',
				'secret:'	: base64.b64encode(b'secret').decode('ascii')
			}
			resp.status_code = 200
		else:
			data = { 'message': f'The user {username} is not authorized' }
			resp.status_code = 401

	js = json.dumps(data)
	resp.set_data(js)
	resp.mimetype = 'application/json'
		
	return resp

if __name__ == '__main__':
	app.run()
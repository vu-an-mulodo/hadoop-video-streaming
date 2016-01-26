from flask import render_template, request, Response, jsonify
from json import dumps
from wsgi import app

__author__ = 'an'

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		try:
			pass
		except (TypeError, ValueError):
			data = {
				'msg': 'Input Error'
			}
			return Response(response=dumps(data), status=422, mimetype='application/json')

		data = {
			'msg': 'msg'
		}
		return jsonify(data)
import subprocess
# from uuid import uuid4
from flask import render_template, request, Response, jsonify
from json import dumps
from wsgi import app
from pydoop import hdfs

__author__ = 'an'

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		# d = uuid4()
		# a = subprocess.Popen(['hadoop', 'fs', '-get', '/caption/DarkKnight.vtt', '/vagrant'], stdout=subprocess.PIPE)
		# print(a)
		f = hdfs.open('/caption/DarkKnight.vtt')
		print(f)
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
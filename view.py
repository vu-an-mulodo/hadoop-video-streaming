from uuid import uuid4
from flask import render_template
from pydoop import hdfs
from wsgi import app

__author__ = 'an'

@app.route('/')
def index():
	n = 'NongNghiep.mp4'
	d = str(uuid4())

	hdfs.get('/video/{}'.format(n), 'static/{}/{}'.format(d, n))
	return render_template('index.html', video='static/{}/{}'.format(d, n))
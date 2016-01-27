from uuid import uuid4
from flask import render_template
from pydoop import hdfs
from wsgi import app

__author__ = 'an'

@app.route('/')
def index():
	n = 'DarkKnight'
	d = str(uuid4())
	f = hdfs.get('/video/{}.mp4'.format(n), '/vagrant/temp/{}/{}.mp4'.format(d, n))
	# s = hdfs.open('caption/{}.vtt'.format(n), 'temp/{}'.format(d))
	return render_template('index.html', video='/vagrant/temp/{}/{}.mp4'.format(d, n), sub='')
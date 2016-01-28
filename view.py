from uuid import uuid4
from flask import render_template
from pydoop import hdfs
from wsgi import app

__author__ = 'an'

@app.route('/')
def index():
	n = 'DarkKnight'
	d = str(uuid4())
	# f = subprocess.Popen(['hadoop', 'fs', '-get', '/caption/DarkKnight.vtt', '/vagrant'], stdout=subprocess.PIPE)
	hdfs.get('/video/{}.mp4'.format(n), 'status/{}/{}.mp4'.format(d, n))
	return render_template('index.html', video='status/{}/{}.mp4'.format(d, n), sub='')
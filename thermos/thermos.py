from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

# html template from http://www.initializr.com/
app = Flask(__name__)
app.config['SECRET_KEY'] = '~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e'

bookmarks = []

def store_bookmark(url):
	bookmarks.append(dict(
		url = url,
		user = 'hotpepper',
		date = datetime.utcnow()
	))

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
	if request.method == 'POST':
		url = request.form['url']
		store_bookmark(url)
		flash("Stored bookmark '%s'"%(url))
		return redirect(url_for('index'))
	return render_template('add.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500

if __name__=='__main__':
	app.run(debug=True)

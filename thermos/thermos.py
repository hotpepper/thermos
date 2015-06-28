from flask import Flask, render_template, url_for
#html template from http://www.initializr.com/

app= Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',
						   title='Title passed from view template',
						   text='text passed from view')

if __name__=='__main__':
	app.run(debug=True)

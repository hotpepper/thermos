from flask import Flask, render_template, url_for
#html template from http://www.initializr.com/

app= Flask(__name__)

class User:
	def __init__(self, firstname, lastername):
		self.firstname = firstname
		self.lastname = lastername
	def initials(self):
		return"%s. %s." %( self.firstname[0], self.lastname[0])
		#"{}. {}.".format(self.firstname[0], self.lastname[0])#2.7+

	def __str__(self):
		return self.firstname+" "+self.lastname

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',
						   title='Title passed from view template',
						   user=User("Seth","Hotpepper"))
@app.route('/add')
def add():
	return render_template('add.html')

if __name__=='__main__':
	app.run(debug=True)

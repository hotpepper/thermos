from flask import Flask, render_template, url_for
#html template from http://www.initializr.com/

app= Flask(__name__)

class User:
	def __init__(self, firstname, lastername):
		self.firstname = firstname
		self.lastname = lastername
	def initials(self):
		return "{}. {}.".format(self.firstname[0], self.lastname[0])

	def __str__(self):
		return self.firstname+" "+self.lastname

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',
						   title='Title passed from view template',
						   user=User("Seth","Hotpepper"))

if __name__=='__main__':
	app.run(debug=True)

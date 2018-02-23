# hello_world.py

from flask import Flask, request, render_template
app = Flask(__name__)

#route to homepage on website
@app.route('/')
def hello_world():
	return 'Hello World!'
    #return render_template('test.html')

@app.route('/about')
def about():
    return 'Hello World! About'

if __name__ == "__main__": 
	app.run(debug=True)
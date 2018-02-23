# views.py

from flask import Flask, render_template, request

from app import app

from development.predict_response import predict_response


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/handle_data', methods = ['POST'])
def handle_data():
    user_input = request.form['ingredients']
    result = predict_response(user_input)
    return render_template("handle_data.html", result = result)


if __name__ == "__main__":
	app.run(debug = True)

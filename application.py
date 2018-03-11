# views.py

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from app import application, db
from app.models import Ing
from development.predict_response import predict_response

# home page
@application.route('/')
def index():
    return render_template("index.html")

# about page
@application.route('/about')
def about():
    return render_template("about.html")

# prediction page
@application.route('/handle_data', methods = ['POST'])
def handle_data():
    user_input = request.form['ingredients']
    result = predict_response(user_input)

    # store user inputs in RDS 
    ing1 = Ing(i_ingredients=request.form['ingredients'])
    db.session.add(ing1)
    db.session.commit()

    return render_template("handle_data.html", result = result)


if __name__ == "__main__":
	application.run(debug = True)

from flask import Flask, request, redirect, url_for
from flask import render_template
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/search',methods=['GET', 'POST'])
def search():
	if request.method == 'GET':
		return render_template("search.html")
	else:
		place_name=request.form['place_name']
		b=exist(place_name)
		if b==True:
			place=get_place_by_name(place_name)
		else:
			create_place(place_name)
			place=get_place_by_name(place_name)
		return redirect(url_for('result', place_name=place_name))

@app.route('/links')
def links():
	return render_template("links.html")

# @app.route("/upload", ["POST"])
# def upload_redirect():
# 	place = request.form["place_name"]
# 	return redirect(url_for("result", place_name=place))

@app.route('/result/<string:place_name>')
def result(place_name):
	b=exist(place_name)
	if b==True:
		place=get_place_by_name(place_name)
		return render_template("result.html", place=place)
	else:
		create_place(place_name)
		place=get_place_by_name(place_name)
		return render_template("result.html", place=place)

if __name__ == '__main__':
	app.run(debug=True)


	
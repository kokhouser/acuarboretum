from flask import render_template, flash, redirect, session, url_for,request
from app import app
from .forms import LoginForm

@app.route("/")
def index():
	return 'Index Page'

@app.route("/map")
def map():
	return render_template('map.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect(url_for('map'))
	return render_template('login.html', form=form)

if __name__ == "__main__":
	app.run()
from flask import render_template, flash, redirect, session, url_for,request
from app import app, db, models
from .forms import LoginForm

@app.route("/")
def index():
	return 'Index Page'

@app.route("/map", methods=['GET', 'POST'])
def map():
	if request.method == 'POST':
		print(request.form['commonName'])
		p = models.Plant(commonName = request.form['commonName'], latinName = request.form['latinName'], latitude = request.form['latitude'], longitude = request.form['longitude'])
		db.session.add(p)
		db.session.commit()
	p = models.Plant.query.all()
	plants = [dict(id=row.id, commonName=row.commonName, latinName=row.latinName, latitude=row.latitude, longitude=row.longitude) for row in p]
	print plants
	return render_template('map.html', plants = plants)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect(url_for('map'))
	return render_template('login.html', form=form)

if __name__ == "__main__":
	app.run()
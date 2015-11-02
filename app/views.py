from flask import render_template, flash, redirect, session, url_for,request
from app import app, db, models
from .forms import LoginForm
from sqlalchemy.sql import exists

@app.route("/")
def index():
	return 'Index Page'

@app.route("/map", methods=['GET', 'POST'])
def map():
	if request.method == 'POST':
		#print (db.session.query(exists().where(models.Plant.longitude == request.form['longitude'])).scalar())
		#print (request.form['ide'])
		if db.session.query(exists().where(models.Plant.id == request.form['ide'])).scalar():
			#print (db.session.query(exists().where(models.Plant.id == request.form['ide'])).scalar())
			p = db.session.query(models.Plant).\
				filter(models.Plant.id==request.form['ide'])
			if 'delete' in request.form and request.form['delete'] == 'delete':
				print ("Here!")
				for i in p:
					print (i)
					db.session.delete(i)
					db.session.commit()
			else:
				for i in p:
				 	print (i)
				 	i.commonName = request.form['commonName']
				 	i.latinName = request.form['latinName']
				 	db.session.commit()
		else:
			p = models.Plant(commonName = request.form['commonName'], latinName = request.form['latinName'], latitude = request.form['latitude'], longitude = request.form['longitude'])
			db.session.add(p)
			db.session.commit()
	p = models.Plant.query.all()
	plants = [dict(id=row.id, commonName=row.commonName, latinName=row.latinName, latitude=row.latitude, longitude=row.longitude) for row in p]
	# Debug statement
	#print plants
	return render_template('map.html', plants = plants)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		return redirect(url_for('map'))
	return render_template('login.html', form=form)

if __name__ == "__main__":
	app.run()
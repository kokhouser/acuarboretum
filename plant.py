from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
	return 'Index Page'

@app.route("/map")
def map():
	return render_template('map.html')

if __name__ == "__main__":
	app.run()
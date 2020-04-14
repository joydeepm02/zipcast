from flask import Flask, escape, request, render_template

from src.gather_weather import get_weather

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/weather', methods = ['POST'])
def weather_handler():
	print(request.method)
	print(request.url)
	zipcode = request.form['user_zipcode']
	data = get_weather(zipcode)
	return render_template('weather.html', title="App", **data)

@app.route('/about')
def about():
	return render_template('about.html', title="About")

@app.route('/tool')
def tool():
    return render_template('tool.html', title="Tool")

# export FLASK_APP = weather-app
# python3 -m flask run
if __name__ == '__main__':
    app.run(debug=False)

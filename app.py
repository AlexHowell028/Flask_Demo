from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/estimate') 
def estimate():
    return render_template('index.html')

@app.route('/about') 
def about():
    return render_template('about.html')

@app.route('/index', methods=['GET','POST'])
def calculate_tank_top(tank_top):
    tank_top= 3.14*['tankRadius']
    return tank_top
    



if __name__ == '__main__':
    app.run(debug=True)


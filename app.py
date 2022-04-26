from flask import Flask
from flask import render_template, request

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

#(Process)Modify app.py to collect the data from your estimate.html form into variables. Calculate the cost estimate
#based on the formulas found in the details section above
#(Output)The calculation should produce a value stored in a varaible that is displayed on estimate.html after processing

@app.route('/index', methods=['GET','POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float (form['radius'])
        height = float (form['height'])
        estimate=radius+height
        return render_template('index.html', data=estimate)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


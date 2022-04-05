from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)

friend_list = [{"name": "Alex Howell", "email":"alex@howell.com"} ]

@app.route('/')
def home():
    return render_template('home.html', pageTitle='Vertical Tank Maintenance', friends = friend_list)

@app.route('/estimate') 
def index():
    return render_template('index.html', pageTitle= 'Estimate')


#@app.route('/home') 
#def friend():
 #   return render_template('home.html', pageTitle= 'Home')


@app.route('/about') 
def mike():
    return render_template('about.html', pageTitle= 'About VTM')

@app.route('/add_friend', methods=['GET', 'POST']) 
def add_friend():
    if request.method == 'POST':
        form = request.form
        fname = form['fname']
        lname = form['lname']
        email = form['email']
        friend_dict = {"name": fname + " " + lname, "email": email}
        friend_list.append(friend_dict)
        return redirect(url_for('index'))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


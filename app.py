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

#(Process)Modify app.py to collect the data from your estimate.html form into variables. Calculate the cost estimate
#based on the formulas found in the details section above
#(Output)The calculation should produce a value stored in a varaible that is displayed on estimate.html after processing

@app.route('/index', methods=['GET','POST'])
def calculate_tank_top(tank_top):
    tank_top= 3.14*['tankRadius']
    return tank_top
    
def calculate_tank_sides(tank_sides):
    tank_sides=2(3.14(['tankRadius']*['tankHeight']))

def calculate_total_area_in(total_area_in):
    tank_area_in= tank_top + tank_sides

def calculate_total_sqft(total_sqft):
    total_sqft=total_area_in/144

def calculate_material_cost(material_cost):
    material_cost= total_sqft*25

def calculate_labor_cost(labor_cost):
    labor_cost=toal_sqft*15

def calculate_total_cost(total_cost):
    total_cost= material_cost + labor_cost
    print (total_cost)



if __name__ == '__main__':
    app.run(debug=True)


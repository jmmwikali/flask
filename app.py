# Import the flask framework
from flask import *

# Below will create the web server based application
app = Flask(__name__)



# Below will create the home route.
# Routing - This is mapping/connecting different resources to different functions. We do this by the help of a decorator
@app.route("/api/home")
def home():
    return jsonify({"message" : "Home Route Accessed"})



# Below is the products route
@app.route("/api/products")
def products():
    return jsonify({"message" : "Welcome to the Products route"})



# Below is a route for addition
@app.route("/api/calc", methods = ["POST"])
def calculator():
    if request.method == "POST":
        number1 = request.form["number1"]
        number2 = request.form["number2"]
        sum = int(number1) + int(number2)
        return jsonify({"The answer is" : sum})
    
# Create a route that is able to calculate the simple interest given the pricipal as 20000, rate as 7% and time as 8 years.
@app.route("/api/simpleinterest")
def s_i():
    principal = 20000
    rate = 7
    time = 8
    simpleinterest = (principal * rate * time) / 100
    return jsonify({"The Simple Interest is" : simpleinterest})




# Below will run the application
app.run(debug=True)
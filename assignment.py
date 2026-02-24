from flask import *

# Import os to navigete the folders in computer
import os

import pymysql

# creation of flask app
app = Flask(__name__)

# Configuring the location where phone images will be stored
app.config["UPLOAD_FOLDER"] = "static/images"


# Smartphones routes start here

# Route to add smartphones
@app.route("/api/add_smartphones", methods=["POST"])
def add_smartphones():
    if request.method == "POST":
        name = request.form["name"]
        brand = request.form["brand"]
        model = request.form["model"]
        storage = request.form["storage"]
        ram = request.form["ram"]
        battery = request.form["battery"]
        price = request.form["price"]
        stock = request.form["stock"]
        photo = request.files["photo"]

        # Extraction of the filename
        filename = photo.filename

        # Extraction of the image's path
        photo_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        # Saving image into new location
        photo.save(photo_path)

        # Creation of connection to db
        connection = pymysql.connect(host="localhost", user="root", password="", database="online")

        # Creation of cursor
        cursor = connection.cursor()

        # Structuring the query to insert data
        sql = "INSERT INTO smartphones (name, brand, model, storage, ram, battery, price, stock, photo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        # Creation of turple to hold data
        data = (name, brand, model, storage, ram, battery, price, stock, filename)

        # Execution of query
        cursor.execute(sql, data)

        # Commit the changes
        connection.commit()


        return jsonify({"message" : "Smartphone added successfully"})
    
# Route to get smartphones
@app.route("/api/get_smartphones")
def get_smartphones():

    # Connection to db
    connection = pymysql.connect(host="localhost", user="root", password="", database="online")

    # Creation of cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # Structuring sql query
    sql = "SELECT * FROM smartphones"

    # Execution of the query
    cursor.execute(sql)

    # Creation of a variable to fetch the data
    smartphones = cursor.fetchall()

    return jsonify(smartphones)

# Smartphones routes end here


# Laptops routes starts here

# Route for adding laptops
@app.route("/api/add_laptops", methods=["POST"])
def add_laptops():
    if request.method == "POST":
        name = request.form["name"]
        brand = request.form["brand"]
        processor = request.form["processor"]
        ram = request.form["ram"]
        storage = request.form["storage"]
        screensize = request.form["screensize"]
        price = request.form["price"]
        stock = request.form["stock"]
        photo = request.files["photo"]

        # Extraction of the filename
        filename = photo.filename

        # Extraction the image's path
        photo_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        # Sacing the image's new path
        photo.save(photo_path)

        # Creation of connection
        connection = pymysql.connect(host="localhost", user="root", password="", database="online")

        # Creation of cursor
        cursor = connection.cursor()

        # Structuring sql query
        sql = "INSERT INTO laptops (name, brand, processor, ram, storage, screensize, price, stock,photo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        # Creating truple to hold data
        data = (name, brand, processor, ram, storage, screensize, price, stock, filename)

        # Execution of the query
        cursor.execute(sql, data)

        # Commit the data
        connection.commit()


        return jsonify({"message" : "Laptop added successfully"})
    

# Route to get laptops
@app.route("/api/get_laptops")
def get_laptops():

    # Connection to db
    connection = pymysql.connect(host="localhost", user="root", password="", database="online")

    # Creation of cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # Structuring sql query
    sql = "SELECT * FROM laptops"

    # Execution of the query
    cursor.execute(sql)

    # Creation of a variable to fetch the data
    laptops = cursor.fetchall()

    return jsonify(laptops)

# laptops routes end here





app.run(debug=True)
from flask import Flask,render_template,redirect,request,jsonify,flash
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

import os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database='rainfall'
)

mycursor = mydb.cursor()

def executionquery(query,values):
    mycursor.execute(query,values)
    mydb.commit()
    return

def retrivequery1(query,values):
    mycursor.execute(query,values)
    data = mycursor.fetchall()
    return data

def retrivequery2(query):
    mycursor.execute(query)
    data = mycursor.fetchall()
    return data

app=Flask(__name__)
app.secret_key='h'

@app.route('/')

def index():
    return render_template('index.html')


@app.route('/About')
def About():
    return render_template('About.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        c_password = request.form['conformpassword']
        if password == c_password:
            query = "SELECT UPPER(email) FROM user2"
            email_data = retrivequery2(query)
            email_data_list = []
            for i in email_data:
                email_data_list.append(i[0])
            if email.upper() not in email_data_list:
                query = "INSERT INTO user2 (name, email, password) VALUES (%s, %s, %s)"
                values = (name, email, password)
                executionquery(query, values)
                flash("Registration successful!", "success")
                return render_template('login.html', message="Successfully Registered!")
            return render_template('register.html', message="This email ID is already exists!")
        return render_template('register.html', message="Conform password is not match!")
    return render_template('register.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        query = "SELECT UPPER(email) FROM user2"
        email_data = retrivequery2(query)
        email_data_list = []
        for i in email_data:
            email_data_list.append(i[0])
        
        if email.upper() in email_data_list:
            query = "SELECT UPPER(password) FROM user2 WHERE email = %s"
            values = (email,)
            password__data = retrivequery1(query, values)
            if password.upper() == password__data[0][0]:
                global user_email
                user_email = email

                return redirect("/home")
            return render_template('login.html', message= "Invalid Password!!")
        return render_template('login.html', message= "This email ID does not exist!")
    return render_template('login.html')

model_path = os.path.join(os.path.dirname(__file__), 'model')

scaler = joblib.load(os.path.join(model_path, 'scalar.joblib'))  

models= joblib.load(os.path.join(model_path, 'random.joblib'))


from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == "POST":
        
        features = [
            float(request.form['blue_band_reflectance']),
            float(request.form['smoothness_entropy']),
            float(request.form['green_band_reflectance']),
            float(request.form['red_band_reflectance']),
            float(request.form['contrast_homogeneity']),
            float(request.form['detected_object_area']),
            float(request.form['latitude']),
            float(request.form['compactness_roundness']),
            float(request.form['edge_detection']),
            float(request.form['sar_backscatter'])
        ]
        
        # Convert input into numpy array for model prediction
        input_features = np.array(features).reshape(1, -1)
        
        
        
        prediction = models.predict(input_features)
        
        # Convert prediction to human-readable output
        result = "Oil Spill Detected" if prediction[0] == 1 else "No Oil Spill Detected"
        print(result)
        
        return render_template('prediction.html', prediction_text=result)
      

    return render_template('prediction.html')


@app.route('/model', methods=['GET', 'POST'])
def model():
    accuracy = None  # Initialize accuracy to prevent undefined variable error
    if request.method == 'POST':
        algorithm = request.form.get('algo')  # Fetch selected algorithm

        # Corrected algorithm names for consistency
        if algorithm == "SVC":
            accuracy = 99.10
        elif algorithm == "RF":
            accuracy = 99.33
        elif algorithm == "XGBoost":
            accuracy = 97.76

    return render_template('model.html', accuracy=accuracy)



@app.route('/home')
def home():
    return render_template('home.html')

           
if __name__=='__main__':
    app.run(debug=True)

# pip install --upgrade scikit-learn


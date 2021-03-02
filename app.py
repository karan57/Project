from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('minip.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Item_Weight=float(request.form['Item_Weight'])
        Item_MRP=float(request.form['Item_MRP'])
        Item_Fat_Content=request.form['Item_Fat_Content']
        if(Item_Fat_Content=='Low Fat'):
            Item_Fat_Content_0=1
            Item_Fat_Content_1=0
        else:
            Item_Fat_Content_0=0
            Item_Fat_Content_1=1
        Outlet_Size=request.form['Outlet_Size']
        if(Outlet_Size=='Large'):
            Outlet_Size_0=1
            Outlet_Size_1=0
            Outlet_Size_2=0
        elif(Outlet_Size=='Medium'):
            Outlet_Size_0=0
            Outlet_Size_1=1
            Outlet_Size_2=0
        else:
            Outlet_Size_0=0
            Outlet_Size_1=0
            Outlet_Size_2=1
        Outlet_Location_Type=request.form['Outlet_Location_Type']
        if(Outlet_Location_Type=='Tier 1'):
            Outlet_Location_Type_0=1
            Outlet_Location_Type_1=0
            Outlet_Location_Type_2=0
        elif(Outlet_Location_Type=='Tier 2'):
            Outlet_Location_Type_0=0
            Outlet_Location_Type_1=1
            Outlet_Location_Type_2=0
        else:
            Outlet_Location_Type_0=0
            Outlet_Location_Type_1=0
            Outlet_Location_Type_2=1
        Outlet_Type=request.form['Outlet_Type']
        if(Outlet_Type=='Supermarket Type1'):
            Outlet_Type_0=1
            Outlet_Type_1=0
            Outlet_Type_2=0
            Outlet_Type_3=0
        elif(Outlet_Type=='Grocery Store'):
            Outlet_Type_0=0
            Outlet_Type_1=1
            Outlet_Type_2=0
            Outlet_Type_3=0
        elif(Outlet_Type=='Supermarket Type3'):
            Outlet_Type_0=0
            Outlet_Type_1=0
            Outlet_Type_2=1
            Outlet_Type_3=0
        else:
            Outlet_Type_0=0
            Outlet_Type_1=0
            Outlet_Type_2=0
            Outlet_Type_3=0
        
            
        prediction=model.predict([[Item_Weight,Item_MRP,Item_Fat_Content_0,Item_Fat_Content_1,Outlet_Size_0,Outlet_Size_1,Outlet_Size_2,Outlet_Location_Type_0,Outlet_Location_Type_1,Outlet_Location_Type_2,Outlet_Type_0,Outlet_Type_1,Outlet_Type_2,Outlet_Type_3]])
        output=round(prediction[0],2)
        
        return render_template('index.html',prediction_text="Outlet Sale is {}".format(output))
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Basic_Classifier.sav', 'rb'))
model1 = pickle.load(open('High_Regression_Log_Life.sav', 'rb'))
model2 = pickle.load(open('Low_Regression.sav', 'rb'))
import csv
BASE_DIR = "C:\\Users\\bdeokar\\Desktop\\Data Science\\Practice\\Diagnosis Batteries\\Battery_Life_Prediction"
import os
@app.route('/',methods=['GET'])
def Home():
    return render_template('result.html')


standard_to = StandardScaler()
@app.route("/", methods=['POST'])
def predict():
    if request.method == 'POST':

        #with open("C:\\Users\\bdeokar\\Desktop\\Data Science\\Practice\\Diagnosis Batteries\\Application_GUI\\test_files\\test_file4.csv") as file:
        with open("C:\\Users\\bdeokar\\Desktop\\Data Science\\Practice\\Diagnosis Batteries\\Application_GUI\\test_files\\test_file1.csv") as file:
            reader = csv.DictReader(file)
            resp = request.form
            for row in reader:
                charge_tym = row['charge tym']
                #charge_tym = round(charge_tym,3)
                log10_Var100_10 = row['log10_Var100-10']
                Intergration = row['intergration.1']
                min1 = row['min']
                Dis_max = row['Dis_max']
                Slope = row['Slope']
                Intercept = row['Intercept']
                iR_min = row['IR_min']
                iR_diff = row['IR_diff']
                Actual_Life=row['Life Cy']
                break


        # charge_tym	=float('charge_tym')
        # log10_Var100_10	=float('log10_Var100_10')
        # Intergration	=float('Intergration')
        # min1=float('min1')
        # Dis_max	=float('Dis_max')
        # Slope	=float('Slope')
        # Intercept	=float('Intercept')
        # iR_min	=float('IR_min')
        # iR_diff	=float('IR_diff')
        if resp.get('Classifier') == '1':
            prediction = model.predict([[float(min1), float(charge_tym), float(log10_Var100_10), float(Intergration)]])
            if prediction == 1:
                prediction1 = model1.predict([[float(min1), float(log10_Var100_10), float(Dis_max), float(Slope),
                                               float(Intercept), float(Intergration), float(charge_tym), float(iR_min),
                                               float(iR_diff)]])
                output1 = prediction1
                # Err = ((float(Actual_Life) - float(output1)) / float(Actual_Life)
                return render_template('Classifier.html',
                                       prediction_text="life cycle is High ",
                                       a=charge_tym, b=log10_Var100_10, c=Intergration, d=min1, e=Dis_max, f=Slope,
                                       g=Intercept, h=iR_min, i=iR_diff, j=Actual_Life)
            else:
                prediction2 = model2.predict([[float(min1), float(log10_Var100_10), float(Dis_max), float(Slope),
                                               float(Intercept), float(Intergration), round(float(charge_tym), 3),
                                               float(iR_min), float(iR_diff)]])
                output2 = prediction2
                return render_template('Classifier.html',
                                       prediction_text="life cycle is Low ",
                                       a=round(float(charge_tym), 3), b=round(float(log10_Var100_10), 3),
                                       c=round(float(Intergration), 3), d=round(float(min1), 3), e=Dis_max, f=Slope,
                                       g=Intercept, h=iR_min, i=iR_diff, j=Actual_Life)
        if resp.get('Regression') == '2':
            prediction = model.predict([[float(min1), float(charge_tym), float(log10_Var100_10), float(Intergration)]])
            if prediction == 1:
                prediction1 = model1.predict([[float(min1), float(log10_Var100_10), float(Dis_max), float(Slope),
                                               float(Intercept), float(Intergration), float(charge_tym), float(iR_min),
                                               float(iR_diff)]])
                output1 = prediction1
                # Err = ((float(Actual_Life) - float(output1)) / float(Actual_Life)
                return render_template('Regression.html',
                                       prediction_text="life cycle is High  {}".format(round(output1[0], 2)),
                                       a=charge_tym, b=log10_Var100_10, c=Intergration, d=min1, e=Dis_max, f=Slope,
                                       g=Intercept, h=iR_min, i=iR_diff, j=Actual_Life)
            else:
                prediction2 = model2.predict([[float(min1), float(log10_Var100_10), float(Dis_max), float(Slope),
                                               float(Intercept), float(Intergration), round(float(charge_tym), 3),
                                               float(iR_min), float(iR_diff)]])
                output2 = prediction2
                return render_template('Regression.html',
                                       prediction_text="life cycle is Low {}".format(round(output2[0], 2)),
                                       a=round(float(charge_tym), 3), b=round(float(log10_Var100_10), 3),
                                       c=round(float(Intergration), 3), d=round(float(min1), 3), e=Dis_max, f=Slope,
                                       g=Intercept, h=iR_min, i=iR_diff, j=Actual_Life)





    else:
        return render_template('result.html')
    #

if __name__=="__main__":
    app.run(debug=True)


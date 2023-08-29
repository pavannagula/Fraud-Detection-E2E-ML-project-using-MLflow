from flask import Flask, render_template, request
import os
import numpy as np
from fraud_detection_project.pipeline.pipeline_prediction import PredictionPipeline

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")

@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Done with Training" 

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            category =float(request.form['category'])
            amt =float(request.form['amt'])
            city_pop =float(request.form['city_pop'])
            trans_month =float(request.form['trans_month'])
            trans_quarter =float(request.form['trans_quarter'])
            Cust_age =float(request.form['Cust_age'])
            city_pop_category =float(request.form['city_pop_category'])
            avg_amount_by_category =float(request.form['avg_amount_by_category'])
            gender_F =float(request.form['gender_F'])
            gender_M =float(request.form['gender_M'])
            trans_year_2019 =float(request.form['trans_year_2019'])
            trans_year_2020 =float(request.form['trans_year_2020'])
       
         
            data = [category,amt,city_pop,trans_month,trans_quarter,Cust_age,city_pop_category,avg_amount_by_category,
                    gender_F,gender_M,trans_year_2019,trans_year_2020]
            data = np.array(data).reshape(1, 12)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = int(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'Issue in the process', e

    else:
        return render_template('index.html')


if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 8080)
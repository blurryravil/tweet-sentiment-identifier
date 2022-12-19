import googletrans
import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from googletrans import Translator
import snscrape.modules.twitter as sntwitter
import pandas as pd

app = Flask(__name__,template_folder='elements')
model = pickle.load(open('Pegasus_Final/Model.pkl','rb'))
vectoriser = pickle.load(open('Pegasus_Final/vectoriser-ngram-(1,2).pkl','rb'))
translator = Translator()

@app.route('/',methods = ['GET']) 
def home():
    return render_template('index.html')

@app.route('/predict',methods = ['POST','GET'])
def predict():
    coment = translator.translate(request.form['coment'])
    handle = request.form['handle']
    query = f"(from:{handle}) until:2020-01-01 since:2010-01-01"
    tweets = []
    i=0
    count =0
    limit = 5             #we can also change the limit as per our wish
    count_racist = 0
    count_non_racist =0
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if count == limit:
            break
        else:
            count = count +1
            tweets.append([tweet.content])
            i=i+1
            temp = translator.translate(tweets[-i][0])
            vector = vectoriser.transform([temp.text])
            predict = model.predict(vector) 
            if predict[0]==0:
                count_non_racist = count_non_racist + 1
            else:
                count_racist = count_racist + 1
    l = []
    vector = vectoriser.transform([coment.text])
    prediction = model.predict(vector)
    print(prediction[0])
    s=""
    if prediction[0]==0:
        if count_racist > 3:
            return render_template('index.html',prediction_text="Your comment is non-racist/positive. You also had a past history of negative comments.")
        else:
            return render_template('index.html',prediction_text="Your comment is non-racist/positive. You got relatively less history of negative comments.")
    else:
        if count_racist > 3:
            return render_template('index.html',prediction_text="Your comment is racist/negative. You also had a past history of negative comments.")
        else:
            return render_template('index.html',prediction_text="Your comment is racist/negative. You got relatively less history of negative comments.")

if __name__ == '__main__':
    app.run(debug=True)

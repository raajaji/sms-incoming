from flask import Flask, url_for
import string
from textblob import TextBlob
import pandas as pd
from textblob.classifiers import NaiveBayesClassifier


app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'


@app.route('/classify/<input>')
def classify(input):
	with open('/sms-incoming/testing.json', 'r') as fp:
		cl = NaiveBayesClassifier(fp, format="json")
		return cl.classify(input)


if __name__ == '__main__':
    app.run()




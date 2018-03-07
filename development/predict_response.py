import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import nltk
import re
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
import pickle
from sklearn.externals import joblib

#from clean_data import clean_data

def predict_response(user_input):
    """
    This function returns cuisine based on user inputs of ingredients.
    Args:
        user_input (str): ingredients
    Returns:
        response_output: predicted cuisine to be displayed on web app
    """
    #load pickle vectorizer & classifier
    vect = joblib.load('./development/ve.pkl')
    classifier = joblib.load('./development/cl.pkl')
    #vectorize the input
    predictors_input = vect.transform([user_input])
    predictors_input.toarray()
    #predict response
    response_output = ''.join(classifier.predict(predictors_input))
    return response_output



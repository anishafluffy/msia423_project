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

def train_model(training_df):
    """
    This function vectorizes the ingredients training dataset using TfidfVectorizer. 
    Next fits a logistic regression model on the vectorized data to classify cuisine. 
    It creates two pickle files, the vectorizer and the model, so that they can be used for prediction.
    
    Arg:
      training_df (DataFrame): data to be used for fitting the model
    
    Returns:
      ve.pkl: vectorizer stored as pickle file to be used for prediction
      cl.pkl: classifier stored as pickle file to be used for prediction
    """
    #instantiate vectorizer
    vect = TfidfVectorizer(stop_words = 'english', #remove standard english stop words
                           ngram_range = (1 , 1), #range of n-values for different n-grams to be extracted
                           analyzer = "word", #feature made of word (not character) n-grams
                           max_df = .57, #ignore terms that have a document frequency higher than threshold 
                           binary = False , 
                           token_pattern = r'\w+' , #what constitutes a “token”
                           sublinear_tf = False
                          )
    #use vectorizer on training corpus
    predictors = vect.fit_transform(df['ingredients_string']).todense()
    #define response
    response = df['cuisine']
    #instantiate model
    clf = LogisticRegression()
    #train the model
    parameters = {'C':[1, 10]}
    classifier = GridSearchCV(clf, parameters)
    classifier = classifier.fit(predictors, response) 
    #create pickle files
    joblib.dump(vect, 've.pkl') 
    joblib.dump(classifier, 'cl.pkl') 

# if __name__ == “__main__“:
#    model(clean_data.clean_data())


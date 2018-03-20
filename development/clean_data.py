import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import nltk
import re
from nltk.stem import WordNetLemmatizer
import logging

# create logging file
logging.basicConfig(filename='log_clean_data.log',level=logging.DEBUG)

def clean_data(path):
	"""
	This function creates a cleaned DataFrame from json file training data 
	
	Args:
		path (str): path to training data json file  
	Returns:
		df: Entire specified dataframe to be used for model training 
	"""
	#import data
	df = pd.read_json(path) 
	logging.debug('File read in from %s', path)
	#clean data
	df['ingredients_clean_string'] = [' , '.join(z).strip() for z in df['ingredients']]  
	df['ingredients_string'] = [' '.join([WordNetLemmatizer().lemmatize(re.sub('[^A-Za-z]', ' ', line)) for line in lists]).strip() for lists in df['ingredients']]       
	logging.info('Data cleaned')
	return df

print("Data has been read and cleaned for model fitting")
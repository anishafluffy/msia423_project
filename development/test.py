import pytest
from clean_data import clean_data	
from predict_response import predict_response

#test the following functions by checking if the function output matches with the desired

def clean_data(path):
	df = clean_data("../data/train.json")
	assert type(df) is pd.core.frame.DataFrame
	assert type(df['ingredients_string'][0]) is str


test = 'garlic'

def predict_response(input_vals):
	result = predict_response(test)
	assert len(result) > 1
	assert type(result) is str


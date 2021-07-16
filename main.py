

import os
import numpy as np
from sklearn import linear_model

""" TERMINOLOGY:
	file   = column
	folder = datasets
"""
def colToList (col):
	with open(col) as f:
		data = f.read()
	lst = data.split("\n")
	lst.pop()
	
	return lst


def Entry (lst, dataset):
	for a in lst:
		pass
		

def getResultsAry (dataset):
	ary = np.array([[]])
	outer = []
	data = colToList("data/"+dataset+"/results.txt")
	for a in data:
		outer.append([a])
		
	data_2 = twoDStrLstToFloat(outer)
	
	return data_2

def twoDStrLstToFloat(lst):
	outer = []
	for item in lst:
		inner = []
		for str in item:
			num = float(str)
			inner.append(num)
		outer.append(inner)
			
	return outer


def getDatasetsName ():
	return os.listdir("data/")


def getColsInDataset (dataset):
	lst = os.listdir("data/"+dataset+"/")
	lst.remove("results.txt")
	return lst


def getIntArray (dataset):
	columns = getColsInDataset(dataset)
	str_lst = []
	for col in columns:
		with open("data/"+dataset+"/"+col) as f:
			raw_data_1 = f.read()
		raw_list_2 = raw_data_1.split("\n")
		raw_list_2.pop()
		inner = []
		for item in raw_list_2:
			inner.append(item)
		str_lst.append(inner)
	int_lst = twoDStrLstToFloat(str_lst)
	ary = np.array(int_lst)
	return ary.T

def guess(dataset):
	x = getIntArray(dataset)
	y = getResultsAry(dataset)
	#print(x,y)
	
	m = linear_model.LinearRegression()
	
	m.fit(x,y)
		   # height, width, recycled, pages
	return m.predict(np.array([[29.7,21,0,240]]))

#print(getIntArray("notebooks"))
#print(getResultsAry("notebooks"))
print(guess("notebooks"))



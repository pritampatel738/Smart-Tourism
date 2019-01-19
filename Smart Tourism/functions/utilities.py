
import sys
import numpy as np
import pandas as pd
import math


def load_data(path):

	# this function reads the data from the directory ......

    data = pd.read_csv(path)
    #print(data.head())
    return data

    pass
    
def head(data,val="not_all"):
	# this function is used to have a look at the data from top ....

	if val == "all":
		print(data)
	
	else:
		print(data.head())

	pass


def tail(data,val=5):

	# this function is used to have a look at the data from bottom ...

	print(data.tail(val))
	pass

import sys
import numpy as np
import pandas as pd
import math


def preprocess_data(data):
    """
        (1) - To convert string values to weight values ......
    """

    regions = ['North','South','East','West','North East','North West','South East','South West']
    region_values = ['1','2','3','4','5','6','7','8']
    types = ['Hill Station','Zoological Park','Beach','Temple']
    types_values = ['100','300','500','800']
    
    data['Region'].replace(regions,region_values,inplace=True)
    data['Type'].replace(types,types_values,inplace=True)

    data['Type'] = data['Type'].astype('float32')
    data['Region'] = data['Region'].astype('float32')
    
    # normalization of data columns ........
    data['Elevation(m)'] = (data['Elevation(m)'] - data['Elevation(m)'].mean())/data['Elevation(m)'].std()
    data['airport_dist(km)'] = (data['airport_dist(km)'] - data['airport_dist(km)'].mean())/data['airport_dist(km)'].std()
    data['railway_dist(km)'] = (data['railway_dist(km)'] - data['railway_dist(km)'].mean())/data['railway_dist(km)'].std()
    data['rating'] = (data['rating'] - data['rating'].mean())/data['rating'].std()
    data['Type'] = (data['Type'] - data['Type'].mean())/data['Type'].std()
    data['Region'] = (data['Region'] - data['Region'].mean())/data['Region'].std()
    
    
    #print(type(data['Type'][0]))
    #print(type(data['Region'][0]))
    #print("Printing preprocessed data : ")
    #print(data.head())
    
    return data
    pass
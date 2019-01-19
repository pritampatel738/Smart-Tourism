import numpy as np
import pandas as pd
import sys
import math
from .similarity_functions import *
from .preprocessing import *


def content_based(user_profile,data):
    sim_dict = {} # to store name value pairs .....
    
    length = len(data) # total length of the data .....
    
    print("The length of the data is : ",length)
    
    names_array = data['Name'] # storing the name columns of data .....
    new_data = data.drop(['Name'],axis=1) # data without 'Name' column ....
    
    #print(new_data[:5])
    
    for i in range(length):
        
        # pick current row .....
        curr_row = new_data.iloc[i]
        
        # now calculate the similarity ........
        curr_row = curr_row.astype('float32') / 1.0
        
        sim_value = cosine_similarity(curr_row,user_profile)
        
        # store the vale in dictionary ......
        sim_dict[names_array[i]] = sim_value
        
        #print("The name and similarity value obtained is : ",names_array[i],sim_value)
        
    
    sim_dict_values = sorted(sim_dict.values()) # sort the dictionary by key value to find top 10 from last ...
    
    return_dict = {} # dictionary to be returned .........
    
    #print("Length of sim_dict_values is : ",len(sim_dict_values))
    #print(sim_dict_values)
    
    for i in range(5):
        value = sim_dict_values[length-i-1]
        
        for j in sim_dict.keys():
            if sim_dict[j] == value:
                
                return_dict[j] = value
                break
            
            
            pass
        pass
        
    print(return_dict)
        
    

def user_profile(data,values):
    """
        returns a numpy array i.e, user profile ......
    """
    #data = preprocess_data(data)
    new_df = data.iloc[values]
    
    features = ['Region','Type','airport_dist(km)','railway_dist(km)','Elevation(m)','rating']
    new_df = new_df[features]
    #print(new_df)
    new_df = np.array(new_df.mean(axis=0))
    
    return new_df

import sys
import math
import pandas as pd
import numpy as np
from functions.similarity_functions import *
from functions.utilities import *
from functions.preprocessing import *
from functions.content_based import *





def main():


    data = pd.read_csv('data/final_data.csv')
    data = data[:49]
    data = preprocess_data(data)
    vals = []
    for i in range(3):
        val = int(input("Select any value : "))
        vals.append(val)

    #print("The selected values are : ",vals)
    profile = user_profile(data,vals)
    print("The profile is : ",profile)

    content_based(profile,data)
    

if __name__ == "__main__":

    main()




# IMPORTING EXERCISE 9 TO BREAK CLOUD_INDEX FUNCTION 

import numpy as np
import Cloud_Index_Function.py

# Define clw array before trying to break function. 
clw = np.array([0, 0, 2, 3, 13])
threshold = 12
cl_in = Exercise9.cloud_index(clw, threshold)
print(cl_in)


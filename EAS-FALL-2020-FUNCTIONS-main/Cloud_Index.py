# Create a Function that takes a list of numbers as input (array) and return the first index where threshold is excceeded. 
import numpy as np

def cloud_index(water_content, threshold):
    """ Computes cloud index of a list of water content values that exceed a defined threshold
    
        input:
        -----
        
            water_content: list of scaler water content variables. 
            
        output:
        ------
    
            The cloud index or (position in array) is printed in the case that the water content variable excceeds the defined threshold.
    
    """
    
   
    b = 0          #Defines first item in list as Index = 0 (Index is the position of the item in the list)
    
    for item in water_content: #For loop set up to compare each item in the list 
        if item > threshold: #If the item excceeds a defined threshold(below), then that item breaks the for loop
            break
        b = b + 1                # Counts the posistion(index) of the item. 
    
    if b == len(water_content):    
        b = -1 
        
    return b  # Determines wheter any item in list excceeds threshold. 
        
            
if __name__ == "__main__":
    clw = np.array([0, 0, 1e-7, 1e-5, 1e-4, 0, 0, 0])
    threshold = 5e-6
    # For threshold above, the first index would be 3 [starts at index = 0, 1, 2, 3, 4]
    cl_in = cloud_index(clw, threshold) 
    print(cl_in)
    
        
    
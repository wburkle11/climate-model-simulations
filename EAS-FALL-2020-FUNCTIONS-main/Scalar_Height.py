# Write a Function that takes water content array and finds the index that first excceeds the threshhold. Then takes that index to find the corresponding cloud base height. 

import numpy as np 
import Cloud_Index

def cloud_base_height(threshold, water_content, height_array):
    """ Returns the scaler value of height given water content and a threshold limit.  

            input:
            -----

                water_content = list of measured values 
                threshold = scalar value of cloudiness limit 
                height_array = list of heights given index location 

            output:
            ------

            "cloud_base_height" cbh = scalar value of height within the height array corresponding to index of water_content 

    """

    #Define Cloud Water Content Array and find the FIRST index postion that exceeds threshold using (cloud_index function).
    cl_in = Cloud_Index.cloud_index(water_content, threshold)
    #Takes the cloud index and assigns it a scalar height associated with the same position. 
    cbh = height_array[cl_in]
    return cbh 
    
    

if __name__ == "__main__":    
    water_content = np.array([0, 0, 2, 3, 13, 15, 46, 234, 123, 56, 7])
    threshold = 12    
    height_array = np.array([0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500])
    cloud_h = cloud_base_height(threshold, water_content, height_array)
    print(cloud_h)
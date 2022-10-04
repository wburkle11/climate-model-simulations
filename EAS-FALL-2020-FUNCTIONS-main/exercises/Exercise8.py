# Create functions for the average, minimun, and maximum values in a given class. 
import numpy as np
import Exercise7 

    
if __name__ == "__main__":
    my_list = Exercise7.operators([4353452, 4, 5, 6, 3, 46, 0, 12345, 76 ,1234 ,3456])  
    print(my_list.average())
    print(my_list.big())
    print(my_list.small())





    my_list2 = np.array([4353452, 4, 5, 6, 3, 46, 0, 12345, 76 ,1234 ,3456])  
    print(my_list2.mean())
    print(my_list2.max())
    print(my_list2.min())
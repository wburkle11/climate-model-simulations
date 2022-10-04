# Create functions for the average, minimun, and maximum values in a given class. 

class operators:

    """ A class is for vector like functions such as lists of numbers or related like operators """

    def __init__(self, input_list):

        #confused on this step
        self.list = input_list

        return 
    def average(self):

        #initialize the sum 
        running_sum = 0 
        #loop over all items in the list
        for a in range(len(self.list)):
            running_sum = running_sum + self.list[a]
        #normalize the average
        running_sum = running_sum/len(self.list)

        #return the final average
        return running_sum 
    
    def small(self):
        # Calculates the Min Value given a list of numbers
        #Add all terms 
        bucket = None 

        for item in self.list:
            if bucket == None: 
                bucket = item 
            if bucket > item:
                bucket = item 
        return bucket 

    def big(self):
        # Calculates the MAX Value 
        # Add all terms 

        bucket = None 

        for item in self.list:
            if bucket == None: 
                bucket = item
            if item > bucket:
                bucket = item

        return bucket 

if __name__ == "__main__":
    my_list = operators([4353452, 4, 5, 6, 3, 46, 0, 12345, 76 ,1234 ,3456])  
    print(my_list.average())
    print(my_list.big())
    print(my_list.small())





    my_list2 = operators([12, 13, 14, 15, 16, 17, 18])  
    print(my_list2.average())
    print(my_list2.big())
    print(my_list2.small())
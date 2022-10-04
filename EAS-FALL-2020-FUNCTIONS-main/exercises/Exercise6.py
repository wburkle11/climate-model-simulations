#Exercise on Classes

class vector:
    """
        A class for vector like lists of number and related operations (min, max, avg) 
    """

    def _init_(self, input_list):
        """ Instantiate a vector object from an input list """

        # store the list in the object
        self.list = input_list 

        # return 
        return 

    def average(self):
        """ Calculates the average of the vector. """

        # initialize the sum 
        running_sum = 0

        # loop over all items in the list
        for i in range(len(self.list)):
            running_sum = running_sum + self.list[i]

        # normalize the average 
        running_sum /= len(self.list)

        #return the average 
        return running_sum 

        #create an instan
    
my_vector = Vector([0,1,5,75,63,234,12])

print(my_vector)
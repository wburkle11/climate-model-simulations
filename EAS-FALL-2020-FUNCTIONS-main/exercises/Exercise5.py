# Write a Maximum Function

def big(terms):
    """ Calculates the Max Value in a given list of number"""

    #Add All Terms 

    basket = None 

    for item in terms:
        if basket == None:
            basket = item 
        if item > basket:
            basket = item
    return basket 

#Terms are listed in (A)

#Define List (A)

a = [3, 6, 7, 5, 12, 64, 78, 2 , 341, 1234, 4]
#Find Value of A

b = big(a)
print(b)
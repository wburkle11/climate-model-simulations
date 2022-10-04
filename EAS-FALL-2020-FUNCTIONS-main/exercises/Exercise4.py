# Write a function that prints the min and max numbers in a given list

def small(terms):
    """Calculates the Min value for a given list of terms

    input
    ===== --> Values in a list that we will refer to as "terms"
    output
    ===== --> Min term in the given list"""

    #Add all terms
    basket = None
    
    for item in terms:
        if basket == None:
            basket = item
        if item < basket:
            basket = item 

    return basket 

# Terms is A 

#Define List
a = [1, 4, 5, 6, 3, 2, 6, 7, 4, 100000000, -7]

#Find Min Value in A
b = small(a)
#Print Output
print(b)
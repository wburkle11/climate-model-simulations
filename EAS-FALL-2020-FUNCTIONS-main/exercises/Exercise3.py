def average(terms):
    """Calculates the average from a list of terms

    input
    =====

    -List of Terms, Terms is variable, Terms is a list of numbers. 

    output
    ======

    -Average value for terms in list. Output will be a scalar value."""

    # Add all terms
    a = 0
    b = 0
    for item in terms:

        a = a+item
        b = b + 1
       # print(a,b)
      
    # Divide by the number of terms in the list. 
    a= a/b
    return a 

list1 = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 2]

avg = average(list1)
print(avg)

list2= [2, 3, 4, 5, 4, 2, 2, 1, 6, 7]

avg = average(list2)
print(avg)

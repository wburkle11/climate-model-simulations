# demonstrates a function 
print("Hello world")

# this is a variable
# = is a operator 
a = 1 
b = 2  

# operators 
# + is an operator
c = a + b 

# print the results 
print(c)

# fundamental types
# numbers (integers, flloating points, lists, strings, dictionaries)
string_variable = "Hello World" # string variable 
print(string_variable)

# define a list of number
a = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0,] 

#define list of strings
b = ["a", "string", "whatever","dum"]

#flow control - for loop
for variable in a:
    #indentation is important
    print(variable)

    # flow control - for loop b
for variable in b:
    pass
    #print(variable)
    print(variable)
# nested for loop 
    for variable in a:
        print(variable)

# print length of a
print("Length of a: ", len(a))     
print("Length of b: ", len(b))
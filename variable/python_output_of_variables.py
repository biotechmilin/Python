#output of variables print() function used in out of variables
x = "Elon bought X"
print(x)
print('*************************************')

#print () function used for multiple variables separated by ,

x = "Elon"
y ="bought"
z = "X"
print(x,y,z)
print('*************************************')

# we can also use + to output multiple variable
x = "Elon"
y ="bought"
z = "X"
print(x+y+z)
print('*************************************')

# for numbers + operator acts as addition
x = 5
y = 4
print(x + y)
print('*************************************')

# you cannot add string and number with + in print function, it will result in error
x = 5
y = "Elon"
print(x+y) #TypeError: unsupported operand type(s) for +: 'int' and 'str'
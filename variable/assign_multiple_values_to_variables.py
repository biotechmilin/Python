
# many values to multiple variables
# note: make sure number of variables match their respective values otherwise it will be an error
x,y,z = "tom", "cat", "harry"
print(x)
print(y)
print(z)
print('*************************************')
#one value to multiple variable
x=y=z = "tom"
print(x)
print(y)
print(z)
print('*************************************')

# unpack a collection

human = ['tesla', 'spacex', 'nuralink']
x,y,z = human
print(x)
print(y)
print(z)
print('*************************************')
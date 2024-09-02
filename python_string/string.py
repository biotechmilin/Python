""" This module is about strings"""

print("hello")
print('hello')
print('*******************************************')

# quotes inside quotes
print("it's alright")
print("its called 'tesla'")
print('its called "tesla"')
print('*******************************************')

# assign string to a variable
a = 'hello'
print(a)
print('*******************************************')

# multiline string
b = ('''tesla is car company,
 tesla is also energy storage company,
 tesla is also AI company''')
print(b)
print('*******************************************')

c= ("""tesla is car company,
 tesla is also energy storage company,
 tesla is also AI company""")
print(c)
print('*******************************************')

# strings in python are arrays
a = 'hello world'
print(a[1])

# loop through the letters in the word "tesla"
a = 'tesla'
for i in a:
    print(i)

#get the length of the string with len() function
print(len(a))

#check string - to check if a certain phrase or character is present in string or not - with 'in' keyword
txt = "the best thing is free things"
print("free" in txt) # this will return a boolean value


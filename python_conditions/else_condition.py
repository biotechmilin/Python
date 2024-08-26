
"""
else is keyword which catches the conditions which was previously not caught
"""
a = 89
b = 34

if b > a:
    print('b is greater than a') # does not meet this condition
elif b == a:
    print('b is equal to a') # does not meet this condition
else:
    print(' b is less than a') # this condition caught by else keyword

print('*******************************')

x = 19
y = 49

if x > y:
    print('x is greater than y')
else:
    print('x is not grater than y')
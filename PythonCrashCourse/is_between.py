"""As an exercise, write a function is_between(x, y, z) that returns True 
if  or False otherwise."""


x = int(input())
y = int(input())
z = int(input())


def is_between(x, y, z):
    return (x <= y <= z)


n = is_between(x, y, z)

if n:
    print('y is between x and z ')
else:
    print('y is not between x and z')
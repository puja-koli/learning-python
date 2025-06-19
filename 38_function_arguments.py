#default argument
def add(a=5,b=6):
    print(a+b)
add()
add(2,3)

#keyword argument
def minus(a,b=1):
    print(a-b)
minus(b=3,a=9)
minus(5,3)

#required argument
def average(a,b):
    print((a+b)/2)
average(5,6)

#variable length argument
def name(**name):
    print(name['fname'],name['mname'],name['lname'])
name(fname='x',mname='y',lname='z')










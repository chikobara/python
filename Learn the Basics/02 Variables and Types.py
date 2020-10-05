#Numbers
myint = 7
print(myint)

#To define a floating point number, you may use one of the following notations:
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

#Strings
#Strings are defined either with a single quote or a double quotes.
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

#The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)
mystring = "Don't worry about apostrophes"
print(mystring)

#Simple operators can be executed on numbers and strings:
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

#Assignments can be done on more than one variable "simultaneously" on the same line like this
a, b = 3, 4
print(a,b)

#Mixing operators between numbers and strings is not supported:
# This will not work!
#one = 1
#two = 2
#hello = "hello"
#print(one + two + hello)

# change this code EXERCISE
#mystring = None
#myfloat = None
#myint = None
# testing code
#if mystring == "hello":
#    print("String: %s" % mystring)
#if isinstance(myfloat, float) and myfloat == 10.0:
#    print("Float: %f" % myfloat)
#if isinstance(myint, int) and myint == 20:
#    print("Integer: %d" % myint)


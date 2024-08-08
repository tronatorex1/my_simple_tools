# 
#   
import time as tm

# *args
def a_unpack(*args):
    print(f"all *args: {args}")
    tm.sleep(.5)

a_unpack(1,2,3,4,5,5,5,5,5,5)


# **kwargs
def b_unpack(**kwargs):
    for x in kwargs.items():
        print(f"Key: {x[0]}, value: {x[1]}")

b_unpack(a=1, b=2, c=3)


# **kwargs all in one shot
def c_unpack(**kwargs):
    print(f"all values: {kwargs}")
    tm.sleep(1)

c_unpack(a=1, b=2, c=3)


# * to pack values into packed variable
def f1(a, b, c, d):
    print(a, b, c, d)

my_list = [1, 2, 3, 4]
f1(*my_list) # here * compacts all values into a single var and passes to the function to unpack


def f2(a,b,c,d): # here the amount of variables (packed) must match with the expected number, otherwise, use *args here
    print(a, b, c, d)

my_list = [1, 2, 3, 4]
f2(*my_list) # here * compacts all values into a single var and passes to the function to unpack







# this function uses unpacking to sum unknown number of arguments
def mySum(*args):
    return sum(args)

mySum(1, 2, 3, 4, 5)
mySum(10, 20)


# unpacking of dictionary items using **
def f(a, b, c):
    print(a, b, c)
 
d = {'a':2, 'b':4, 'c':10}
f(**d) # this converts using ** to kwargs
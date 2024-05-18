# This script shows IDIOMS in python 
#   IDIOMS are better ways to do things, since python is an idiomatic language

# Use enumerate to know the pos of the element iterated
l = (-10,20,-30,40,-50,60,-70,80,-90)
for pos, value in enumerate(l):
    print(f"pos={pos} : value={value}")

try:
    x = next(i for i, n in enumerate(l) if n > 70) # searched the first matching value (pos of value > 70)
except StopIteration:
    print('No positive numbers')
else:
    print('The index of the first positive number is: ', x)

# Sorting the enumerated list
print(sorted(l))
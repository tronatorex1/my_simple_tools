# This is the difference between assigning b = a (called Aliasing or referencing) and Cloning (creating a different memory allocated var
#    with the same contents)

# Aliasing (assigns various vars to the same memory space/values)
a = [1,2,3,4,5,6,0]
b = a
print(a, b)
print(id(a), id(b))

b[0] = 'AAAAA'
print(a, b)
print(id(a), id(b))


# Cloning (creates a diff variable with the same contents)
c = [1,2,3,4]
d = c[:]
print(c, d)
print(id(c), id(d))

d[0] = 'BBBB'
print(c, d)
print(id(c), id(d))


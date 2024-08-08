# This is an example on Generators and how to create them using List/Tuple Comprenhensions. A generator can be inviked only once, afterward, it will delete its instructions...
#   With tuples, the output object is a generator that requires a loop to iterate over it. With lists, the output object is a simple list with the results of the instruction

# output = tuple
gen_t = (x**2 for x in range(3))
print(gen_t)

for i in gen_t:
    print(f" · {i}")
 

# output = list
gen_l = [x**2 for x in range(3)] 
print(gen_l)
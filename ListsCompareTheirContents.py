# This is an example on how to find the values not present in a list regarding another list
#   
list_1 = [1, 3, 5]
list_2 = [1, 2, 3, 4, 5]

solution_1 = list(set(list_2) - set(list_1))
solution_2 = list(set(list_1) ^ set(list_2)) # this one looks for pos0_list1 = pos0_list2 and so on...
solution_3 = list(set(list_1).symmetric_difference(set(list_2)))

print(f"Solution 1: {solution_1}")
print(f"Solution 2: {solution_2}")
print(f"Solution 3: {solution_3}")

# the other way around
list_1 = [1, 3, 5, 7, 9]
list_2 = [1, 5, 2]

solution_1 = list(set(list_2) - set(list_1))
solution_2 = list(set(list_1) ^ set(list_2)) # this one looks for pos0_list1 = pos0_list2 and so on...
solution_3 = list(set(list_1).symmetric_difference(set(list_2)))

print(f"Solution 1: {solution_1}")
print(f"Solution 2: {solution_2}")
print(f"Solution 3: {solution_3}")
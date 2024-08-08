# This is an example on how to merge 2 dict vars
#
a = {"a": 1, "b": 2}
b = {"c": 3, "d": 4}

merged = a | b
print(merged)
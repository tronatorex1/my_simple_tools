# This is an example on how to pass args and keyword arguments to functions. Everything before the Dict = args ; Dict and on = kwargs
#   args are non-dict types; kwargs are dict types

def some_function(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")


some_function(1, 2, 3, a=4, b=5, c=6)
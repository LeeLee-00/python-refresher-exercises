#Methodof collecting multiple arguments ina  single variable.

def multiply(*args):
    print(args)
    total = 1 
    for arg in args:
        total = total * arg
    return total



def add(x, y):
    return x + y

nums = {"x": 18, "y": 25}
print(add(**nums)) # simplified when used dicitionaries



def apply(*args, operator):
    if operator == "*":
        return multiply(args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."
    
print(apply(1,3,6,7, operator="+"))
def add(x,y): # x and y are parameters
    result = x + y
    print(result)

add(5,3) # 5 and 3 are arguments 

# Another example with any parameters

def say_hello(name,surname):
    print(f"Hello!, {name} {surname}")

say_hello("Lee","Noel") # wont run cause function has no paramters


# Divide Function

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")

divide(dividend=15, divisor= 0)
def add(x, y):
    return (x + y)

add(5,8)
result = add(5, 8)
print(result)



# Back to the divid functoin

def divide(dividend, divisor):
    if divisor != 0:
        return(dividend / divisor)
    else:
        return("You fool!")

divide(dividend=15, divisor= 0) 
print(result)

# Note - usually not recommended to retrn different types of data from a funciton - just not advised to.
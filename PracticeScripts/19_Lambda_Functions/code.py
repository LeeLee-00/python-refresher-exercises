#Operate on inputs and returns some outputs
add = lambda x, y: x + y
# Lambda meant to be short functions without using a name...

print(add(5,7))


# To treat as a single unit

print((lambda a, b: a + b)(9 ,7)) # Not really useuful....


def double(x):
    return x * 2

sequence = [1,3,5,9]
doubled = [double(x)for x in sequence]

# With Lambda (with map)
doubled = list(map(double, sequence))
print(doubled)
# To view the results - you must return it with a list as map returns a map object.
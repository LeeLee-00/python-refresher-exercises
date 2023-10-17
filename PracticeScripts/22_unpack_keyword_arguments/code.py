""" def named(**kwargs): # The "*" collects keyword arguments "kwargs"
    print(kwargs)
named(name="Bob", age=25)
 """

#Another method

def named(**kwargs):
    print(kwargs)


# Print nicely formula

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name = "Bob", age=25)

## now with both

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1,3,5, name="bob", age=25)
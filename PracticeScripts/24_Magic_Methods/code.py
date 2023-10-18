class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #def __str__(self): # Magic method due to two __ for turning oject in string
     #   return f"Person {self.name}, {self.age} years old"

    def __repr__(self):
        return f"<Person({self.name}, {self.age})>" # could also call method manually like:
    # bob.__repr__()
    # repr - used to print unambigous reprisentation of an object which you can use to print out that method

bob = Person("Bob", 35)
print(bob) #Print <__main__.Person object at 0x000002B9B4D168D0> - default string of all objects



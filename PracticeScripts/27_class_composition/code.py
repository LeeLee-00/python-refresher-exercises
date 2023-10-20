# Class Composition

# Counterpart to inheritance to build out classes to use other classes
# Simplier - reduces complexity of code

class BookShelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f"BookSehlf with {len(self.books)} books."

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}" 

book = Book("Falling Up")
book2 = Book("Falling down")
shelf = BookShelf(book, book2)
print(shelf)

#Inheritance - Book has a "Bookshelf"
#Class Composition - Books has many books
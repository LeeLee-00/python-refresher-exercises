class ClassTest:
    def instanfce_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")
    
    @staticmethod
    def static_method():
        print("Called static_method")

ClassTest.static_method()

# Factory Example

class Book:
    TYPES = ("hardcover", "paperback","manga")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighng {self.weight}g>" 
    
    @classmethod
    def hardcover(cls,name,page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls,name,page_weight):
        return Book(name, Book.TYPES[1], page_weight)

    @classmethod
    def manga(cls,name,page_weight):
        return Book(name, Book.TYPES[2], page_weight)

book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python Training 101", 600)
manga = Book.manga("Tokyo Ghoul", 1000)

print(book)
print(light)
print(manga)
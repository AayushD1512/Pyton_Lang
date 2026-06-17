# Create a class Book with attributes title and author.

# Implement __str__() so that printing the object displays "Title by Author".
# Implement __len__() so that len(book) returns the length of the title.
# Create two Book objects and test these methods.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return len(self.title)
    

book1= Book("The Monk", "Sarah Joseph Martina")

book2= Book("The Alchemist", "Paulo Coelho")

print(book1)
print(book2)
print(len(book1))

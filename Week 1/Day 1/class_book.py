class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
    
    def get_name(self):
        return self.name
    
    def get_author(self):
        return self.author 
    
    def get_pages(self):
        return self.pages

    

book = Book("My Book", "Nicole", 200)

print(book.name)
print(book.author)
print(book.pages)               
print(book.get_name())
from user import User
from typing import List, Dict

class Library:

    def __init__(self):
        self.user_records: List[User] = []
        self.books_avaliable : Dict[str:list[str]] = {}
        self.rented_books : Dict[str: Dict[str:int]] = {}

    def get_book(self, author, book_name, day_to_return, user:User):
        if book_name in self.books_avaliable[author]:
            self.books_avaliable[author].remove(book_name)
            user.books.append(book_name)

            if user.user_name in self.rented_books:
                self.rented_books[user.username][book_name] = day_to_return
            else:
                self.rented_books[user.user_name] = {book_name : day_to_return}

            return f"{book_name} successfully rented for the next {day_to_return} days!"      

        for data in self.rented_books.values():
            if book_name in data:
                return f'The book "{book_name}" is already rented and will be available in {data[book_name]} days!'

    def return_book(self, author, book_name, user:User):
        if book_name in self.rented_books[user.user_name]:
            del self.rented_books[user.user_name]
            user.books.remove(book_name)
            self.books_avaliable[author].append(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"    

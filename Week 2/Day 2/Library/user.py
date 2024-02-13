from typing import List


class User:

    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.books : List[str] = []

    def info(self):
        return ','.join(sorted(self.books))

    def __repr__(self):
        return f"{self.user_id},{self.user_name },{self.books}"
        
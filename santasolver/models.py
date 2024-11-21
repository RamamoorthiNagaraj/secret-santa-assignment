# models.py
class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Employee({self.name}, {self.email})"

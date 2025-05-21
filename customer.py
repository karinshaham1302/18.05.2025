from typing import override

class Customer:
    def __init__(self, name: str, email: str, __id: int):
        self.name = name
        self.email = email
        self.__id = __id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if value > 0:
            self.__id = value
        else:
            print("id must be a positive number.")

    @override
    def __str__(self) -> str:
        return f"Customer {self.name} (ID: {self.__id}) Email: {self.email}"

    @override
    def __repr__(self) -> str:
        return f"Customer(name='{self.name}', email='{self.email}', id={self.__id})"

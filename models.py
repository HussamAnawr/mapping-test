
class User:

    def __init__(self, name, email) -> None:
        self.id = None
        self.name = name
        self.email = email
        self.things = []

    def __repr__(self) -> str:
        return f"<User name={self.name} email={self.email}>"
    def add_thing(self, thing):
        self.things.append(thing)
    

class Car:
    def __init__(self, name) -> None:
        self.name=name
    def __repr__(self) -> str:
        return f"<Car name={self.name}>"
    

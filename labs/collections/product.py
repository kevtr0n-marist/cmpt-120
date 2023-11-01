import uuid

class Product:

    def __init__(self, name, description, cost):
        self.uuid = str(uuid.uuid4())
        if type(name) != str:
            raise TypeError("'name' must be a string.")
        if type(description) != str:
            raise TypeError("'description' must be a string.")
        if type(cost) != float:
            raise TypeError("'cost' must be a float.")
        #  Ensure product name is capitalized.
        self.name = name
        self.description = description
        self.cost = cost

    def __eq__(self, value) -> bool:
        if isinstance(value, Product):
            return value.uuid == self.uuid or value.name == self.name
        return False
    
    def __hash__(self) -> int:
        return hash(self.name)
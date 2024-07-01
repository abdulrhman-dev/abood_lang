from tokens import Variable
from tree import Node


class Data:
    def __init__(self):
        self.variables: dict[Node] = {}

    def read_all(self):
        return self.variables

    def read(self, name):
        return self.variables[name]

    def assign(self, token: Variable, value):
        variable_name = token.value
        self.variables[variable_name] = value

    def display(self, data):
        if isinstance(data, str):
            # from interpreter import Interpreter

            if data in self.variables:
                # expression = Interpreter(self.read(data), memory)

                return self.read(data)

            raise Exception(f"Variable {str(data)} doesn't exist")

        return data

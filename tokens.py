class Token:
    def __init__(self, value, type, start_index, end_index):
        self.value = value
        self.type = type
        self.start_index = start_index
        self.end_index = end_index

    def __repr__(self) -> str:
        # return f'{str(self.value)}'
        # return f'{str(self.value)}>{str(self.type)[:3]}'
        return f'"{str(self.value)}>{str(self.type)[:3]}"'


class Integer(Token):
    def __init__(self, value, start_index=None, end_index=None):
        super().__init__(int(value), 'integer', start_index, end_index)


class Float(Token):
    def __init__(self, value, start_index=None, end_index=None):
        super().__init__(float(value), 'float', start_index, end_index)


class Operation(Token):
    def __init__(self, value, start_index=None, end_index=None):
        super().__init__(value, 'operation', start_index, end_index)

    def execute(self, num1, num2):
        match self.value:
            case '+':
                return num1 + num2
            case '-':
                return num1 - num2
            case '*':
                return num1 * num2
            case '/':
                return num1 / num2


class Variable(Token):
    def __init__(self, value, start_index=None, end_index=None):
        super().__init__(value, 'variable', start_index, end_index)


class Declaration(Token):
    def __init__(self, value, start_index=None, end_index=None):
        super().__init__(value, 'declaration', start_index, end_index)


class BooleanOperator(Token):
    def __init__(self, value, start_index=None, end_index=None):
        super().__init__(value, 'boolean_operator', start_index, end_index)

    def execute(self, comp1, comp2=None):
        match self.value:
            case 'and':
                return int(comp1 and comp2)
            case 'or':
                return int(comp1 or comp2)
            case 'not':
                return int(not comp1)


class Comparision(Token):
    def __init__(self, value, start_index, end_index):
        super().__init__(value, 'comparision', start_index, end_index)

    def execute(self, num1, num2):
        match self.value:
            case '>':
                return int(num1 > num2)
            case '<':
                return int(num1 < num2)
            case '==':
                return int(num1 == num2)
            case '<=':
                return int(num1 <= num2)
            case '>=':
                return int(num1 >= num2)


class Keyword(Token):
    def __init__(self, value, start_index, end_index):
        super().__init__(value, 'keyword', start_index, end_index)

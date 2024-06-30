class Token:
    def __init__(self, value, term_type, start_index, end_index):
        self.value = value
        self.term_type = term_type
        self.start_index = start_index
        self.end_index = end_index

    def __repr__(self) -> str:
        return str(self.value)


class Integer(Token):
    def __init__(self, value, start_index, end_index):
        super().__init__(int(value), 'integer', start_index, end_index)


class Float(Token):
    def __init__(self, value, start_index, end_index):
        super().__init__(float(value), 'float', start_index, end_index)


class Operation(Token):
    def __init__(self, value, start_index, end_index):
        super().__init__(value, 'operation', start_index, end_index)

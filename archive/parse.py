from tokens import Token


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.index = 0
        self.parse_tree = []
        self.current_token = tokens[0]

    def move(self):
        self.index += 1

        if (self.index < len(self.tokens)):
            self.current_token = self.tokens[self.index]

    def factor(self):
        if (self.current_token.term_type == 'integer' or self.current_token.term_type == 'float'):
            return self.current_token

    def term(self):

        term_tree = self.factor()
        self.move()

        while (self.current_token.value == '*' or self.current_token.value == '/'):
            left_node = term_tree
            self.move()
            right_node = self.current_token

            term_tree = [left_node, '*', right_node]
            self.move()
        return term_tree

    def expression(self):

        self.parse_tree = self.term()

        while (self.current_token.value == '+' or self.current_token.value == '-'):
            operation = self.current_token.value

            left_node = self.parse_tree
            self.move()

            right_node = self.term()

            self.parse_tree = [left_node, operation, right_node]

    def parse(self):
        return self.expression

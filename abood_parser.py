from tokens import Token, Integer, Operation, BooleanOperator
from tree import BinaryTree
from tree import Node


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.index = 0
        self.current_token = tokens[0]

    def move(self):
        self.index += 1
        if (self.index < len(self.tokens)):
            self.current_token = self.tokens[self.index]

    def factor(self) -> Node:
        if (self.current_token.type == 'integer' or self.current_token.type == 'float'):
            return Node(self.current_token)
        elif (self.current_token.type == 'variable'):
            return Node(self.current_token)
        elif (self.current_token.value == '('):
            self.move()
            return self.expression()
        elif (self.current_token.value == '-'):
            self.move()
            unary_root = Node(Operation('*'))
            unary_root.left = self.factor()
            unary_root.right = Node(Integer(-1))
            return unary_root

    def term(self) -> Node:
        term = self.factor()
        self.move()

        while (self.current_token.value == '*' or self.current_token.value == '/'):
            left_node = term

            operation = Node(self.current_token)

            self.move()
            right_node = self.factor()

            term = operation
            term.left = left_node
            term.right = right_node

            self.move()
        return term

    def expression(self) -> Node:
        expression = self.term()
        while (self.current_token.value == '+' or self.current_token.value == '-'):
            left_node = expression

            operation = Node(self.current_token)
            self.move()

            right_node = self.term()

            expression = operation
            expression.left = left_node
            expression.right = right_node

        return expression

    def comparision_expression(self):
        not_comparision = False

        if (self.current_token.value == 'عكس'):
            not_comparision = True
            self.move()

        comparision_expression = self.expression()

        if (self.current_token.type == 'comparision'):
            left_node = comparision_expression

            comparision = Node(self.current_token)
            self.move()

            right_node = self.expression()

            comparision_expression = comparision
            comparision_expression.left = left_node
            comparision_expression.right = right_node

        if (not_comparision):
            not_comparision_tree = Node(BooleanOperator('عكس'))
            not_comparision_tree.left = comparision_expression
            not_comparision_tree.right = Node(Integer(0))

            return not_comparision_tree

        return comparision_expression

    def bool_expression(self):
        bool_expression = self.comparision_expression()

        if (self.current_token.value == 'و' or self.current_token.value == 'أو'):
            left_node = bool_expression

            operation = Node(self.current_token)
            self.move()

            right_node = self.comparision_expression()

            bool_expression = operation
            bool_expression.left = left_node
            bool_expression.right = right_node

        return bool_expression

    def if_statement(self):
        action = {
            'action': 'if',
            'elif': []
        }
        self.move()
        action['expr'] = self.bool_expression()
        self.move()
        action['do'] = self.statement()

        while (self.current_token.value == 'غير إذا'):
            sub_action = {'action': 'if'}
            self.move()
            sub_action['expr'] = self.bool_expression()
            self.move()
            sub_action['do'] = self.statement()

            action['elif'].append(sub_action)

        if (self.current_token.value == 'غير ذلك'):
            self.move()
            action['else'] = self.statement()

        return action

    def statement(self):
        expression_types = ['integer', 'float',
                            'operation', 'variable', 'boolean_operator']

        if (self.current_token.value == 'إذا'):
            return self.if_statement()

        elif (self.current_token.type == 'declaration'):
            self.move()
            variable_name = self.current_token
            self.move()

            if (self.current_token.value == '='):
                statement_tree = Node(self.current_token)
                statement_tree.left = Node(variable_name)
                self.move()

                statement_tree.right = self.bool_expression()

                return {'expr': statement_tree}
        elif self.current_token.type in expression_types:
            return {'expr': self.bool_expression()}

    def parse(self):
        return self.statement()

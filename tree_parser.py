from tokens import Token
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self, root=None):
        if (root is None):
            return
        self.root = Node(root)

    @staticmethod
    def post_order_traversal(start: Node):
        result = []

        if (start.left):
            result.extend(BinaryTree.post_order_traversal(start.left))

        if (start.right):
            result.extend(BinaryTree.post_order_traversal(start.right))

        result.append(start.value)

        return deque(result)

    @staticmethod
    def printTree(node, level=0):
        if node != None:
            BinaryTree.printTree(node.left, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.value))
            BinaryTree.printTree(node.right, level + 1)


class TreeParser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.index = 0
        self.current_token = tokens[0]

    def move(self):
        self.index += 1
        if (self.index < len(self.tokens)):
            self.current_token = self.tokens[self.index]

    def factor(self) -> Node:
        if (self.current_token.term_type == 'integer' or self.current_token.term_type == 'float'):
            return Node(self.current_token)
        elif (self.current_token.value == '('):
            self.move()
            return self.expression_tree()

    def term_tree(self) -> Node:
        term_tree = self.factor()
        self.move()

        while (self.current_token.value == '*' or self.current_token.value == '/'):
            left_node = term_tree

            operation = Node(self.current_token)

            self.move()
            right_node = self.factor()

            term_tree = operation
            term_tree.left = left_node
            term_tree.right = right_node

            self.move()

        return term_tree

    def expression_tree(self) -> Node:
        expression_tree = self.term_tree()
        while (self.current_token.value == '+' or self.current_token.value == '-'):
            left_node = expression_tree

            operation = Node(self.current_token)
            self.move()

            right_node = self.term_tree()

            expression_tree = operation
            expression_tree.left = left_node
            expression_tree.right = right_node

        return expression_tree

    def parse(self):
        output_tree = BinaryTree()
        output_tree.root = self.expression_tree()
        return output_tree

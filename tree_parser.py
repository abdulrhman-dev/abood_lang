from tokens import Token


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

    def post_order_traversal(self, start: Node):
        result = []

        if (start.left):
            result.extend(self.post_order_traversal(start.left))

        if (start.right):
            result.extend(self.post_order_traversal(start.right))

        result.append(start)

        return result


class TreeParser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.index = 0
        self.current_token = tokens[0]

    def move(self):
        self.index += 1
        if (self.index < len(self.tokens)):
            self.current_token = self.tokens[self.index]

    def term_tree(self) -> Node:
        if (self.index + 1 >= len(self.tokens)):
            return Node(self.current_token)

        next_token = self.tokens[self.index + 1]

        if not (next_token.value == '*' or next_token.value == '/'):
            return Node(self.current_token)

        term_tree = None

        while (next_token.value == '*' or next_token.value == '/'):
            if (term_tree is not None):
                left_node = term_tree
            else:
                left_node = Node(self.tokens[self.index])
            self.move()

            operation = Node(self.tokens[self.index])
            self.move()

            right_node = Node(self.tokens[self.index])

            term_tree = operation
            term_tree.left = left_node
            term_tree.right = right_node

            if (self.index + 1 >= len(self.tokens)):
                break

            next_token = self.tokens[self.index + 1]

        return term_tree

    def expression_tree(self) -> BinaryTree:
        expression_node_tree = self.term_tree()

        if (self.index + 1 >= len(self.tokens)):
            expression_tree = BinaryTree()
            expression_tree.root = expression_node_tree
            return expression_tree

        next_token = self.tokens[self.index + 1]

        while (next_token.value == '+' or next_token.value == '-'):
            left_node = expression_node_tree
            self.move()

            operation = Node(self.current_token)
            self.move()

            right_node = self.term_tree()

            expression_node_tree = operation
            expression_node_tree.left = left_node
            expression_node_tree.right = right_node

            if (self.index + 1 >= len(self.tokens)):
                break

            next_token = self.tokens[self.index + 1]

        expression_tree = BinaryTree()
        expression_tree.root = expression_node_tree
        return expression_tree

    def parse(self):
        return self.expression_tree()

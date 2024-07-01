from tree_parser import Node, BinaryTree
from tokens import Integer, Float
from collections import deque
from data import Data


class Interpreter:
    def __init__(self, tree: Node, memory: Data) -> None:
        self.tree = tree
        self.expressions: deque[Node] = None
        self.memory = memory

    def interpret(self):

        if (self.tree.node.value == '='):
            self.memory.assign(
                self.tree.left.node, self.evaluate_expression(self.tree.right))
            return

        return self.evaluate_expression(self.tree)

    def evaluate_expression(self, working_tree):
        self.expressions = BinaryTree.post_order_traversal(working_tree)

        if (len(self.expressions) < 3):
            return self.memory.display(self.expressions[0].value)
        while (len(self.expressions) > 1):
            self.expressions = self.excute_expression()

        return self.expressions[0].value

    def excute_expression(self):
        if (self.expressions[2].type != 'operation'):
            left_node = self.expressions.popleft()
            self.expressions = self.excute_expression()
            self.expressions.appendleft(left_node)
        else:
            num1 = self.memory.display(self.expressions[0].value)
            num2 = self.memory.display(self.expressions[1].value)
            operation: Node = self.expressions[2]

            self.expressions.popleft()
            self.expressions.popleft()
            self.expressions.popleft()

            result = operation.execute(num1, num2)
            if (result.is_integer()):
                result = Integer(result)
            else:
                result = Float(result)

            self.expressions.appendleft(result)

        return self.expressions

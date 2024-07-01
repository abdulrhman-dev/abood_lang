from tokens import Integer, Float
from data import Data
from tree import BinaryTree, Node


class Interpreter:
    def __init__(self, action: dict, memory: Data) -> None:
        self.action = action
        self.memory = memory

    def interpret(self):
        if ('action' in self.action):
            return
        expression = self.action['expr']

        if (expression.node.value == '='):
            self.memory.assign(
                expression.left.node, self.evaluate_expression(expression.right))
            return

        return self.evaluate_expression(expression)

    def evaluate_expression(self, working_tree):
        expressions = BinaryTree.post_order_traversal(working_tree)

        if (len(expressions) < 3):
            return self.memory.display(expressions[0].value)
        while (len(expressions) > 1):
            expressions = self.excute_expression(expressions)

        return expressions[0].value

    def excute_expression(self, expressions):
        allowed_operations = ['operation', 'boolean_operator', 'comparision']
        if (expressions[2].type not in allowed_operations):
            left_node = expressions.popleft()
            expressions = self.excute_expression(expressions)
            expressions.appendleft(left_node)
        else:
            num1 = self.memory.display(expressions[0].value)
            num2 = self.memory.display(expressions[1].value)
            operation: Node = expressions[2]

            expressions.popleft()
            expressions.popleft()
            expressions.popleft()

            result = operation.execute(num1, num2)
            if (result.is_integer()):
                result = Integer(result)
            else:
                result = Float(result)

            expressions.appendleft(result)

        return expressions

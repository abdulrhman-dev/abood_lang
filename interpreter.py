from tokens import Integer, Float
from data import Data
from tree import BinaryTree, Node


class Interpreter:
    def __init__(self,  memory: Data) -> None:
        self.memory = memory
        self.output = []

    def interpret(self, action):
        if ('action' in action):
            if (action['action'] == 'if'):
                return self.interpret_if(action)

        expression = action['expr']

        if (expression.node.value == '='):
            self.memory.assign(
                expression.left.node, self.evaluate_expression(expression.right))
            return

        value = self.evaluate_expression(expression)
        self.output.append(value)
        return value

    def interpret_if(self, action):
        if (self.evaluate_expression(action['expr'])):
            self.interpret(action['do'])
            return True

        if ('elif' in action):
            for else_if in action['elif']:
                condition = self.interpret(else_if)
                if (condition):
                    return True

            if ('else' in action):
                self.interpret(action['else'])

        return False

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

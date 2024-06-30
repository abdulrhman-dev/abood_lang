from tree_parser import Node, BinaryTree
from tokens import Integer, Float
from collections import deque


def interpret(tree: Node):
    expressions: list[Node] = BinaryTree.post_order_traversal(tree)

    if (len(expressions) < 3):
        return expressions[0]
    while (len(expressions) > 1):
        expressions = excute(expressions)

    return expressions[0].value


def excute(expressions: deque):
    if (expressions[2].term_type != 'operation'):
        left_node = expressions.popleft()
        expressions = excute(expressions)
        expressions.appendleft(left_node)
    else:
        num1 = expressions[0]
        num2 = expressions[1]
        operation: Node = expressions[2]

        expressions.popleft()
        expressions.popleft()
        expressions.popleft()

        result = operation.execute(num1.value, num2.value)
        if (result.is_integer()):
            result = Integer(result)
        else:
            result = Float(result)

        expressions.appendleft(result)

    return expressions

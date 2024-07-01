from collections import deque


class Node:
    def __init__(self, value):
        self.node = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.node)


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

        result.append(start.node)

        return deque(result)

    @staticmethod
    def printTree(node, level=0):
        if node != None:
            BinaryTree.printTree(node.left, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.node))
            BinaryTree.printTree(node.right, level + 1)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return self.value


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def post_order_traversal(self, start: Node):
        result = []

        if (start.left):
            result.extend(self.post_order_traversal(start.left))

        if (start.right):
            result.extend(self.post_order_traversal(start.right))

        result.append(start)

        return result


tree_1 = BinaryTree('3')

tree_1.root.left = Node('4')

tree_2 = BinaryTree('4')
tree_2.root.right = tree_1.root

print(tree_2.post_order_traversal(tree_2.root))

from lexer import Lexer
from tree_parser import TreeParser, BinaryTree

# while True:
print("Initilized abood-lang...")

# exp = input('>')
lexer = Lexer('(5+3*2)*((3+5)*7 + 6)*3+5*6-3')
tokens = lexer.tokenize()
print(tokens)
new_parser = TreeParser(tokens)

expressions_tree = new_parser.parse()
print(BinaryTree.post_order_traversal(expressions_tree.root))
BinaryTree.printTree(expressions_tree.root)

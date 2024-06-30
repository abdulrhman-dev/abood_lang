from lexer import Lexer
from tree_parser import TreeParser, BinaryTree
from interpreter import interpret

# while True:
print("Initilized abood-lang...")
# while True:
#     exp = input('>')
lexer = Lexer('store name = 5 * 2')
tokens = lexer.tokenize()
print(tokens)
# new_parser = TreeParser(tokens)

# expressions_tree = new_parser.parse()
# output = interpret(expressions_tree.root)

# print(output)

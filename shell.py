from lexer import Lexer
from tree_parser import TreeParser, BinaryTree
from interpreter import Interpreter
from data import Data
# while True:
print("Initilized abood-lang...")


memory = Data()
# while True:
#     exp = input('>')
lexer = Lexer('5 >= 1 and not 1')
tokens = lexer.tokenize()
print(tokens)
new_parser = TreeParser(tokens)

expressions_tree = new_parser.parse()
# BinaryTree.printTree(expressions_tree)

interpreter = Interpreter(expressions_tree, memory)

output = interpreter.interpret()

print('Result', output)
# print(memory.read_all())

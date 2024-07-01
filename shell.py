from lexer import Lexer
from abood_parser import Parser
from tree import BinaryTree, Node
from interpreter import Interpreter
from data import Data
# while True:
print("Initilized abood-lang...")


memory = Data()
# while True:
#     exp = input('>')

lexer = Lexer('if 5 >= 3 do store n = 4 elif 3 == 3 if 2 == 2 do 2 else 3')
tokens = lexer.tokenize()
print(tokens)
new_parser = Parser(tokens)

actions = new_parser.parse()
print(actions)
# BinaryTree.printTree(expressions_tree)

# interpreter = Interpreter(actions, memory)

# output = interpreter.interpret()

# print('Result', output)
# # print(memory.read_all())

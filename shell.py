from lexer import Lexer
from abood_parser import Parser
from tree import BinaryTree, Node
from interpreter import Interpreter
from data import Data
import json
# while True:
print("Initilized abood-lang...")


memory = Data()
# while True:
#     exp = input('>')

lexer = Lexer(
    'if 5 <= 3 do if not 3 == 3 do store n = 4 elif not 3 == 3 do 3 elif not 1 and 1 do 4 else 5+5 else if 3<1 do 3 else 4')
tokens = lexer.tokenize()
# print(tokens)
new_parser = Parser(tokens)

action = new_parser.parse()
# print(action)

# BinaryTree.printTree(expressions_tree)

interpreter = Interpreter(memory)

interpreter.interpret(action)

print(interpreter.output)

# print('Result', output)
print(memory.read_all())

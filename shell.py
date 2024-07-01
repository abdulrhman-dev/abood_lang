from lexer import Lexer
from abood_parser import Parser
from tree import BinaryTree, Node
from interpreter import Interpreter
from data import Data
import sys

if (len(sys.argv) < 2):
    raise Exception('a file directory must be passed ')

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')
    memory = Data()
    for line in lines:
        lexer = Lexer(line)
        tokens = lexer.tokenize()
        if (len(tokens) == 0):
            continue
        parser = Parser(tokens)
        action = parser.parse()
        interpreter = Interpreter(memory)
        interpreter.interpret(action)
        outputs = interpreter.output
        for output in outputs:
            print(output)

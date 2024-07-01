from lexer import Lexer
from abood_parser import Parser
from tree import BinaryTree, Node
from interpreter import Interpreter
from data import Data

with open('code.abd', 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')
    memory = Data()
    for line in lines:
        lexer = Lexer(line)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        action = parser.parse()
        interpreter = Interpreter(memory)
        interpreter.interpret(action)
        outputs = interpreter.output
        for output in outputs:
            print(output)

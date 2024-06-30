from lexer import Lexer
from parse import Parser

print("Initilized abood-lang...")

# exp = input('>')
lexer = Lexer('1+2*5')
tokens = lexer.tokenize()
parseTree = Parser(tokens)
parseTree.parse()

from lexer import Lexer
from tree_parser import TreeParser

print("Initilized abood-lang...")

# exp = input('>')
lexer = Lexer('2 * 3 + 5* 4')
tokens = lexer.tokenize()
# parseTree = Parser(tokens)
# parseTree.parse()
# print(tokens)

new_parser = TreeParser(tokens)
new_parser.parse()

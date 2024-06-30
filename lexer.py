import re
from collections.abc import Iterable


class Token:
    def __init__(self, value, term_type, start_index, end_index):
        self.value = value
        self.term_type = term_type
        self.start_index = start_index
        self.end_index = end_index

    def __repr__(self) -> str:
        return str(self.value)


class Integer(Token):
    def __init__(self, value, start_index, end_index):
        super().__init__(int(value), 'integer', start_index, end_index)


class Float(Token):
    def __init__(self, value, start_index, end_index):
        super().__init__(float(value), 'float', start_index, end_index)


class Operation(Token):
    def __init__(self, value, start_index, end_index):
        super().__init__(value, 'operation', start_index, end_index)


class Lexer:
    def __init__(self, exp) -> None:
        self.tokens = []
        self.exp = exp

    def tokenize(self) -> list[Token]:
        integerRegex = r'(?<!\.)\d+(?!\.)'
        floatRegex = r'\d+\.\d*'
        operationRegex = r'[+*\-]'

        self.extract(re.finditer(
            integerRegex, self.exp), Integer)
        self.extract(re.finditer(
            floatRegex, self.exp), Float)
        self.extract(re.finditer(
            operationRegex, self.exp), Operation)

        self.tokens = sorted(self.tokens, key=lambda t: t.start_index)

        return self.tokens

    def extract(self, itr: Iterable[re.Match[str]], TermType: Token):
        for match in itr:
            value = match.string[match.start():match.end()]

            self.tokens.append(TermType(value, match.start(), match.end()))


lex = Lexer('52+3 * 4.4 + 22 * 44 + 26')

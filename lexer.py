import re
from collections.abc import Iterable
from tokens import *


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

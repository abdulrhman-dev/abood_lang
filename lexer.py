import re
from collections.abc import Iterable
from tokens import *


class Lexer:
    def __init__(self, exp) -> None:
        self.tokens = []
        self.exp = exp

    def tokenize(self) -> list[Token]:
        declrations = ['store']

        integer_regex = r'(?<!\.)\d+(?!\d*\.)'
        float_regex = r'\d+\.\d*'
        operationRegex = r'[\(\)+*/=-]'
        declrationRegex = f'({'|'.join(declrations)})'
        wordsRegex = fr'(?!{'|'.join(declrations)})\b[a-zA-Z]+\b'

        self.extract(re.finditer(
            integer_regex, self.exp), Integer)
        self.extract(re.finditer(
            float_regex, self.exp), Float)
        self.extract(re.finditer(
            operationRegex, self.exp), Operation)
        self.extract(re.finditer(
            declrationRegex, self.exp), Declaration)
        self.extract(re.finditer(
            wordsRegex, self.exp), Variable)

        self.tokens = sorted(self.tokens, key=lambda t: t.start_index)

        return self.tokens

    def extract(self, itr: Iterable[re.Match[str]], TermType: Token):
        for match in itr:
            value = match.string[match.start():match.end()]

            self.tokens.append(TermType(value, match.start(), match.end()))

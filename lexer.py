import regex as re
from collections.abc import Iterable
from tokens import *


class Lexer:
    def __init__(self, exp) -> None:
        self.tokens = []
        self.exp = exp

    def tokenize(self) -> list[Token]:
        main_keywords = ['store', 'and', 'or', 'not']

        integer_regex = r'(?<!\.\d*)\d+(?!\d*\.)'
        float_regex = r'\d+\.\d*'
        operationRegex = r'([\(\)+*/-]|(?<!=|<|>)[=](?!=))'
        declrationRegex = r'store(?=\s+)'
        booleanRegex = r'(and|or|not)(?=\s+)'
        wordsRegex = fr'(?!{'|'.join(main_keywords)})\b[a-zA-Z]+\b'
        comparisonRegex = r'((>=)|(<=)|(==)|(>)|(<))'

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
        self.extract(re.finditer(
            booleanRegex, self.exp), BooleanOperator)
        self.extract(re.finditer(
            comparisonRegex, self.exp), Comparision)

        self.tokens = sorted(self.tokens, key=lambda t: t.start_index)

        return self.tokens

    def extract(self, itr: Iterable[re.Match[str]], TermType: Token):
        for match in itr:
            value = match.string[match.start():match.end()]

            self.tokens.append(TermType(value, match.start(), match.end()))

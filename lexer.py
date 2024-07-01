import regex as re
from collections.abc import Iterable
from tokens import *


class Lexer:
    def __init__(self, exp) -> None:
        self.tokens = []
        self.exp = exp

    def tokenize(self) -> list[Token]:
        avoid_words = ['خزن', 'و', 'أو',
                       'عكس', 'إذا', 'نفذ', 'غير ذلك', 'غير إذا', 'ذلك', 'غير']
        keywords = ['إذا', 'نفذ', 'غير ذلك', 'غير إذا']

        integer_regex = r'(?<!\.\d*)\d+(?!\d*\.)'
        float_regex = r'\d+\.\d*'
        operationRegex = r'([\(\)+*/-]|(?<!=|<|>)[=](?!=))'
        declrationRegex = r'خزن(?=\s+)'
        keywordsRegex = fr'({'|'.join(keywords)})'
        booleanRegex = r'(و|أو|عكس)(?=\s+)'
        wordsRegex = fr'(?!{'|'.join(avoid_words)
                            })\b[\u0621-\u064A\u0660-\u0669_]+\b'
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
        self.extract(re.finditer(
            keywordsRegex, self.exp), Keyword)

        self.tokens = sorted(self.tokens, key=lambda t: t.start_index)

        return self.tokens

    def extract(self, itr: Iterable[re.Match[str]], TermType: Token):
        for match in itr:
            value = match.string[match.start():match.end()]

            self.tokens.append(TermType(value, match.start(), match.end()))

from enum import Enum, auto
import re

# ----------------------------
# Token Types
# ----------------------------
class TokenType(Enum):
    # Keywords
    MOVE = auto()
    TURN = auto()
    REPEAT = auto()
    FLIP = auto()
    PRINT = auto()

    # Literals
    NUMBER = auto()
    IDENTIFIER = auto()

    # Symbols
    LBRACKET = auto()
    RBRACKET = auto()

    EOF = auto()

# ----------------------------
# Token Object
# ----------------------------
class Token:
    def __init__(self, type, lexeme, literal=None, line=1):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __repr__(self):
        return f"{self.type}({self.lexeme}, {self.literal})"
    
# ----------------------------
# Tokenizer
# ----------------------------
class Scanner:
    keywords = {
        "MOVE": TokenType.MOVE,
        "TURN": TokenType.TURN,
        "REPEAT": TokenType.REPEAT,
        "FLIP": TokenType.FLIP,
        "PRINT": TokenType.PRINT,
    }

    def __init__(self, source: str):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

    # ----------------------------
    # Main entry
    # ----------------------------
    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    # ----------------------------
    # Core scanning
    # ----------------------------
    def scan_token(self):
        c = self.advance()

        if c == "[":
            self.add_token(TokenType.LBRACKET)

        elif c == "]":
            self.add_token(TokenType.RBRACKET)

        elif c.isspace():
            if c == "\n":
                self.line += 1

        elif c.isdigit():
            self.number()

        elif c.isalpha():
            self.identifier()

        else:
            print(f"[ERROR] Unexpected character '{c}' at line {self.line}")

    # ----------------------------
    # Identifiers / Keywords
    # ----------------------------
    def identifier(self):
        while self.peek().isalnum():
            self.advance()

        text = self.source[self.start:self.current]

        token_type = self.keywords.get(text, TokenType.IDENTIFIER)
        self.add_token(token_type)

    # ----------------------------
    # Numbers
    # ----------------------------
    def number(self):
        while self.peek().isdigit():
            self.advance()

        value = self.source[self.start:self.current]
        self.add_token(TokenType.NUMBER, int(value))

    # ----------------------------
    # Helpers
    # ----------------------------
    def advance(self):
        c = self.source[self.current]
        self.current += 1
        return c

    def peek(self):
        if self.is_at_end():
            return "\0"
        return self.source[self.current]

    def is_at_end(self):
        return self.current >= len(self.source)

    def add_token(self, type, literal=None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(type, text, literal, self.line))
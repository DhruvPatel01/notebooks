import re

token_types = {
    '(': "LEFT_PAREN",
    ')': "RIGHT_PAREN",
    ',': "COMMA",
    '=': "ASSIGN",
    '+': "PLUS",
    '-': "MINUS",
    '*': "ASTERISK",
    '/': "SLASH",
    '^': "CARET",
    '~': "TILDE",
    '!': "BANG",
    '?': "QUESTION",
    ':': "COLON"
}

def eat_whitespace(source, i=0):
    while source[i] in (' \t\n'): i += 1
    return i


class  Scanner:
    def __init__(self, source):
        self.source = source
        tokens = []
        
        i = 0
        while i < len(source):
            i = eat_whitespace(source, i)
            if source[i] in token_types:
                tokens.append( (token_types[source[i]], ) )
                i += 1
            else:
                j = i
                while source[j] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    j += 1
                    if j == len(source): break
                tokens.append( ("NAME", source[i:j]) )
                i = j
        tokens.append( ("EOF", ) )

        self.tokens = tokens
        self.i = 0

    def consume(self):
        self.i += 1
        return self.tokens[self.i-1]

    def look_ahead(self, j):
        return self.tokens[self.i+j]
        

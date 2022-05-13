# Variables

INT = 'INT' # integers
FLO = 'FLO' # floating point numbers
CHA = 'CHA' # char
STR = 'STR' # string
ARR = 'ARR' # array
TUP = 'TUP' # tuple
DIC = 'DIC' # dictionary
BOO = 'BOO' # boolean
CLA = 'CLA' # class
FUN = 'FUN' # function

# Operators

PLS = 'PLS'
SUB = 'SUB'
MUL = 'MUL'
DIV = 'DIV'

# Alphanumeric

RPS = 'RPS'
LPS = 'LPS'
DIGITS = '1234567890'
LOWER = 'abcdefghijklmnopqrstuvwxyz'
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Classes

class Error():
    def __init__(self, err, details) -> None:
        self.err = err
        self.details = details
    
    def stringify(self):
        result = f'{self.error_name}: {self.details}'

class IllegalCharError(Error):

    def __init__(self, details) -> None:
        super().__init__('Illegal Character', details)


class Token ():
    def __init__(self, _type, value):
        self.type = _type
        self.value = value 

    def __repr__(self) -> str:
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

class Lexer ():
    def __init__(self, txt) -> None:
        self.txt = txt
        self.pos = -1
        self.currchar = None
        self.advance

    def advance(self):
        self.pos += 1
        self.currchar = self.txt[self.pos] if self.pos < len(self.txt) else None

    def tokenize(self):
        tokens = []

        while self.currchar != None:
            if self.currchar in ' \t':
                self.advance()
            elif self.currchar in DIGITS:
                tokens.append(self.numerate)
            
            match self.currchar:
                case '+':
                    tokens.append(Token(PLS))
                case '-':
                    tokens.append(Token(SUB))
                case '*':
                    tokens.append(Token(MUL))
                case '/':
                    tokens.append(Token(DIV))
                case '(':
                    tokens.append(Token(LPS))
                case ')':
                    tokens.append(Token(RPS))
                case _ :
                    char = self.currchar
                    self.advance
                    return [], IllegalCharError("'" +  char + "'")

        return tokens, None

    def numerate (self):
        num_str = ''
        dots = 0

        while self.currchar != None and self.currchar in DIGITS + '.':
            if self.currchar == '.':
                if dots == 1: break
                dots += 1
                num_str += '.'
            else:
                num_str += self.currchar

        if dots == 0:
            return Token(INT, int(num_str))
        elif dots == 1:
            return Token(FLO, float(num_str))

# Run

def run(txt):
    lexer = Lexer(txt)
    tokens, error = lexer.tokenize()

    return tokens, error
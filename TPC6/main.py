import ply.lex as lex
import sys

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'in':'IN',
    'char': 'CHAR',
    'int': 'INT',
    'short': 'SHORT',
    'long': 'LONG',
    'string': 'STRING',
    'while': 'WHILE',
    'for': 'FOR',
    'function': 'FUNCTION',
    'program': 'PROGRAM'
}

tokens = [
    # comment
    'COMMENT',
    # abre e fecha
    'L_BRACKET','R_BRACKET','L_BRACE','R_BRACE','L_PAR','R_PAR',
    # aritmetica
    'SUM','MUL','DIV','SUB','ASSIGN','RANGE',
    # cond
    'EQUAL','DIF','NOT','LESS','MORE','LESS_E','MORE_E',
    # declaracoes
    'VAR','NUM','SEMICOLON','COMMA'
 ] + list(reserved.values())

def t_COMMENT(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    return t

t_ignore = f' \n\t\r'

# abre e fecha
t_L_BRACKET = r'\['
t_R_BRACKET = r'\]'
t_L_BRACE = r'{'
t_R_BRACE = r'}'
t_L_PAR = r'\('
t_R_PAR = r'\)'
# tipos
t_CHAR = r'char'
t_SHORT = r'short'
t_INT = r'int'
t_LONG = r'long'
t_STRING = r'string'
# loops
def t_WHILE(t):
    r'while'
    return t

def t_FOR(t):
    r'for'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

# artimetica
t_SUM = r'\+'
t_MUL = r'\*'
t_DIV = r'/'
t_SUB = r'-'

def t_ASSIGN(t):
    r'='
    return t

t_RANGE = r'..(?=\d+)'
# cond
t_EQUAL = r'=='
t_DIF = r'!='
t_NOT = r'!'
t_LESS = r'<'
t_MORE = r'>'
t_LESS_E = r'<='
t_MORE_E = r'>='
t_IN = r'in'
# func
def t_FUNCTION(t): 
    r'function'
    return t
def t_PROGRAM(t):
     r'program'
     return t
# declaracoes
def t_VAR(t):
    r'[_a-z]\w*'
    t.type = reserved.get(t.value,'VAR')
    return t


def t_NUM(t):
    r'[+\-]?\d+'
    t.value = int(t.value)
    return t

t_SEMICOLON = r';'
t_COMMA = r','

def t_error(t):
    print('Carater não válido')
    t.lexer.skip(1)

if __name__ == '__main__':
    data = sys.stdin.read() if len(sys.argv) == 1 else open(sys.argv[1]).read()
    lexer = lex.lex()
    lexer.input(data)
    toks = []
    for tok in lexer:
        toks.append(tok)
    print(f'''Tamanho da lista: {len(toks)}
Lista:
{toks}''')

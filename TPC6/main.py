import ply.lex as lex
import sys

tokens = (
    # comment
    'COMMENT'
    # abre e fecha
    'COMMENT_L','COMMENT_R','L_BRACKET','R_BRACKET','L_BRACE','R_BRACE','L_PAR','R_PAR',
    # tipos
    'CHAR','SHORT','INT','LONG','STRING',
    # loops
    'WHILE','FOR',
    # declaracoes
    'VAR','ASSIGN','NUM','SEMICOLON','COMMA'
    # aritmetica
    'SUM','MUL','DIV','SUB','RANGE'
    # cond
    'EQUAL','DIF','NOT','LESS','MORE','LESS_E','MORE_E', 'IN'
    # func
    'FUNCTION','PROGRAM'
)

t_ignored = r' \t\n\r'
# comments
t_COMMENT = r'//.*'
# abre e fecha
t_COMMENT_L = r'/\*'
t_COMMENT_R = r'\*/'
t_L_BRACKET = r'['
t_R_BRACKET = r']'
t_L_BRACE = r'{'
t_R_BRACE = r'}'
t_L_PAR = r'('
t_R_PAR = r')'
# tipos
t_CHAR = r'char'
t_SHORT = r'short'
t_INT = r'int'
t_LONG = r'long'
t_STRING = r'string'
# loops
t_WHILE = r'while'
t_FOR = r'for'
# declaracoes
t_VAR = r'[_a-z]\w*'
t_ASSIGN = r'='

def t_NUM(t):
    r'[+\-]?\d+'
    t.value = int(t.value)
    return t

t_SEMICOLON = r';'
t_COMMA = r','
# artimetica
t_SUM = r'\+'
t_MUL = r'\*'
t_DIV = r'/'
t_SUB = r'-'
t_RANGE = r'..'
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
t_FUNCTION = r'function'
t_PROGRAM = r'PROGRAM'

def t_error(t):
    print('Carater não válido')
    t.lexer.skip(1)

if __name__ == '__main__':
    data = sys.stdin.read() if len(sys.argv) == 0 else open(sys.argv).read()
    lexer = lex.input(data)
    toks = []
    for tok in lexer:
        toks.append(tok)

import ply.lex as lex

tokens = [
    'int',
    'long',
    'float',
    'double',
    'char',
    'string',
    'boolean',
    'void',
    'null',
    'true',
    'false',
    'assign',
    'for',
    'while',
    'if',
    'else',
    'switch',
    'case',
    'return',
    'then',
    'do',
    'default',
    'break',
    'call',
    'and',
    'or',
    'not',
    'plus',
    'minus',
    'times',
    'divide',
    'equals',
    'greater',
    'lower',
    'greater_or_equal',
    'lower_or_equal',
    'l_parenthesis',
    'r_parenthesis',
    'end',
    'print',
    'function',
    'identifier',
    'number_unsigned',
    'text'
]

t_int = r'đźŤŽ'
t_long = r'đźŤŚ'
t_float = r'đźŤ‡'
t_double = r'đźŤ’'
t_char = r'đźŤ“'
t_string = r'đźŤ‰'
t_boolean = r'âť”'
t_void = r'đźŚź'
t_null = r'âšˇď¸Ź'
t_true = r'âś…'
t_false = r'đźš«'
t_assign = r'âŹ®'
t_for = r'â†Şď¸Ź'
t_while = r'đź”„'
t_if = r'âŹ¸'
t_else = r'âŹŻ'
t_switch = r'đź’ˇ'
t_case = r'đź›„'
t_return = r'đź“¬'
t_then = r'đź’Ą'
t_do = r'â›Ź'
t_default = r'đźŤž'
t_break = r'đźŤş'
t_call = r'đź“ž'
t_and = r'đź…°ď¸Ź'
t_or = r'đź…ľď¸Ź'
t_not = r'âť•'
t_plus = r'âž•'
t_minus = r'âž–'
t_times = r'âś–ď¸Ź'
t_divide = r'âž—'
t_equals = r'đźŚ—'
t_greater = r'đźŚť'
t_lower = r'đźŚš'
t_greater_or_equal = r'đźŚ’'
t_lower_or_equal = r'đźŚ”'
t_l_parenthesis = r'đźŚś'
t_r_parenthesis = r'đźŚ›'
t_end = r'đź”š'
t_print = r'đź–¨ď¸Ź'
t_function = r'âš™ď¸Ź'

t_ignore  = ' \t'

def t_identifier(t):
    r'[_a-zA-Z][_a-zA-Z0-9]*'
    t.value = str(t.value)
    return t

def t_number_unsigned(t):
    r'\d+.{0,1}\d*'
    try:
        t.value = int(t.value)
    except:
        t.value = float(t.value)
    return t

def t_text(t):
    r'\".*\"'
    t.value = str(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

with open('test.txt') as f:
    lines = f.readlines()

content = "".join(lines)

lexer.input(content)

#while True:
    #tok = lexer.token()
    #if not tok:
    #    break
    #else:
        #print(tok)
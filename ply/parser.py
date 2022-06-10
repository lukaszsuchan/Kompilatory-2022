import ply.yacc as yacc
import sys
from scanner import tokens

tab = 0
case = None
error = False
output = ""

def tabs(x):
    ret = ""
    for i in range(x):
        ret += '\t'
    return ret

def formater(x):
    global tab
    a = ["if", "for", "while", "else:", "def", "elif"]
    tmp = ""
    x = str(x).split('\n')
    for line in x:
        tmp += tabs(tab) + line + '\n'
        if a.__contains__(line.split(' ')[0]):
            tab += 1
        if line.split(' ').__contains__('|'):
            tab -= 1

    ret = ""
    for line in tmp.split('\n'):
        if not line.__contains__('|'):
            ret += line + '\n'
    return ret

def p_start(p):
    'start : program'
    p[0] = p[1]
    p[0] = formater(p[0])
    global output
    if not error:
        output = p[0]
    with open('output.py', 'w') as f:
        f.write(output)


def p_program(p):
    'program : blok'
    p[0] = p[1]

def p_blok(p):
    '''
    blok : blok_deklaracji end blok_instrukcji end
        | end blok_instrukcji end
        | blok_deklaracji end end
        | end end
    '''
    if len(p) == 5:
        p[0] = p[1] + p[3]
    elif len(p) == 4 and p[1] == "đź”š":
        p[0] = p[2]
    elif len(p) == 4:
        p[0] = p[1]
    else:
        p[0] = ""

def p_blok_deklaracji(p):
    '''
    blok_deklaracji : dek_funs
    '''
    p[0] = p[1]

def p_dek_funs(p):
    '''
    dek_funs :
        | dek_fun
        | dek_fun dek_funs
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = ""

def p_dek_fun(p):
    '''
    dek_fun : function var_sym identifier l_parenthesis arguments r_parenthesis instrukcjas return wyrazenie end
        | function void identifier l_parenthesis arguments r_parenthesis instrukcjas end
    '''
    if len(p) == 11:
        p[0] = "def " + p[3] + "(" + p[5] + "):\n" + p[7] + "return " + p[9] + "\n|\n\n"
    else:
        p[0] = "def " + p[3] + "(" + p[5] + "):\n" + p[7] + "\n|\n"

def p_arguments(p):
    '''
    arguments :
        | var_sym identifier
        | var_sym identifier arguments
    '''
    if len(p) == 3:
        p[0] = p[2]
    elif len(p) == 4:
        p[0] = p[2] + ", " + p[3]
        if p[0][len(p[0])-2] == ",":
            p[0] = str(p[0])[0:len(p[0])-2]
    else:
        p[0] = ""

def p_blok_instrukcji(p):
    '''
    blok_instrukcji : instrukcjas
    '''
    p[0] = p[1]

def p_instrukcjas(p):
    '''
    instrukcjas :
        | instrukcja
        | instrukcja instrukcjas
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = ""

def p_instrukcja(p):
    '''
    instrukcja : instr_inicjuj end
        | instr_podstaw end
        | instr_wywolaj end
        | instr_if end
        | instr_while end
        | instr_for end
        | wypisz end
        | instr_switch end
    '''
    p[0] = tabs(tab) + p[1] + "\n"

def p_instr_inicjuj(p):
    '''
    instr_inicjuj : var_liczba_sym identifier assign liczba
        | var_liczba_sym identifier assign null
        | string identifier assign text
        | string identifier assign null
    '''
    if p[4] == "âšˇď¸Ź":
        p[4] = "None"
    p[0] = p[2] + " = " + str(p[4])

def p_instr_podstaw(p):
    '''
    instr_podstaw : identifier assign wyrazenie
        | identifier assign null
    '''
    p[0] = p[1] + " = " + p[3]

def p_instr_wywolaj(p):
    '''
    instr_wywolaj : call identifier l_parenthesis wyrazenies r_parenthesis
    '''
    p[0] = p[2] + "(" + p[4] + ")"

def p_wyrazenies(p):
    '''
    wyrazenies :
        | wyrazenie
        | wyrazenie wyrazenies
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + ", " + p[2]
        if p[0][len(p[0]) - 2] == ",":
            p[0] = str(p[0])[0:len(p[0]) - 2]
    else:
        p[0] = ""

def p_instr_if(p):
    '''
    instr_if : if warunek then instrukcja instrukcjas
        | if warunek then instrukcja instrukcjas else instrukcja instrukcjas
    '''
    if len(p) == 6:
        p[0] = "if " + p[2] + ":\n" + p[4] + p[5] + " |"
    elif len(p) == 9:
        p[0] = "if " + p[2] + ":\n" + p[4] + p[5] + "|\n" + "else:\n" + p[7] + p[8] + "|"

def p_instr_while(p):
    '''
    instr_while : while warunek do instrukcjas
    '''
    p[0] = "while " + p[2] + ":\n" + p[4] + "|"


def p_instr_for(p):
    '''
    instr_for : for for_warunek do instrukcjas
    '''
    p[0] = "for " + p[2] + ":\n" + p[4] + "|"

def p_wypisz(p):
    '''
    wypisz : print wyrazenie
        | print text
    '''
    p[0] = "print(" + p[2] + ")"

def p_instr_switch(p):
    '''
    instr_switch : switch l_parenthesis wyrazenie r_parenthesis case_blok case_bloks case_default
    '''
    p[0] = str(p[5])[2:] + p[6] + p[7]
    p[0] = case(p[0], p[3]) + "|"

def case(x, k):
    return x.replace("¿", k)

def p_case_blok(p):
    '''
    case_blok : case l_parenthesis wyrazenie r_parenthesis then instrukcjas end
        | case l_parenthesis wyrazenie r_parenthesis then instrukcjas break end
    '''
    p[0] = "elif " + "¿" + " == " + p[3] + ":\n" + p[6] + '|\n'

def p_case_default(p):
    '''
    case_default : default then instrukcjas end
    '''
    p[0] = "else:\n" + p[3]

def p_case_bloks(p):
    '''
    case_bloks :
        | case_blok
        | case_blok case_bloks
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = ""

def p_var_sym(p):
    '''
    var_sym : var_liczba_sym
        | string
        | boolean
        | char
    '''
    if p[1] == "đźŤ‰":
        p[0] = "string"
    elif p[1] == "âť”":
        p[0] = "boolean"
    elif p[1] == "đźŤ“":
        p[0] = "char"
    else:
        p[0] = p[1]

def p_var_liczba_sym(p):
    '''
    var_liczba_sym : int
        | long
        | float
        | double
    '''
    if p[1] == "đźŤŽ":
        p[0] = "int"
    elif p[1] == "đźŤŚ":
        p[0] = "long"
    elif p[1] == "đźŤ‡":
        p[0] = "float"
    elif p[1] == "đźŤ’":
        p[0] = "double"

def p_wyrazenie(p):
    '''
    wyrazenie : skladnik skladniks
        | true
        | false
        | text
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    elif len(p) == 2:
        if p[1] == "âś…":
            p[0] = "True"
        elif p[1] == "đźš«":
            p[0] = "False"
        else:
            p[0] = p[1]

def p_skladnik(p):
    '''
    skladnik : czynnik czynniks
    '''
    p[0] = str(p[1]) + p[2]

def p_skladniks(p):
    '''
    skladniks :
        | oper_add skladnik
        | oper_add skladnik skladniks
    '''
    if len(p) == 3:
        p[0] = " " + p[1] + " " + p[2]
    elif len(p) == 4:
        p[0] = " " + p[1] + " " + p[2] + p[3]
    else:
        p[0] = ""

def p_oper_add(p):
    '''
    oper_add : plus
        | minus
    '''
    if p[1] == "âž–":
        p[0] = "-"
    elif p[1] == "âž•":
        p[0] = "+"

def p_oper_mul(p):
    '''
    oper_mul : times
        | divide
    '''
    if p[1] == "âś–ď¸Ź":
        p[0] = "*"
    elif p[1] == "âž—":
        p[0] = "/"

def p_czynnik(p):
    '''
    czynnik : identifier
        | liczba
        | instr_wywolaj
        | wyr_w_naw
    '''
    p[0] = p[1]

def p_czynniks(p):
    '''
    czynniks :
        | oper_mul czynnik
        | oper_mul czynnik czynniks
    '''
    if len(p) == 3:
        p[0] = " " + p[1] + " " + p[2]
    elif len(p) == 4:
        p[0] = " " + p[1] + " " + p[2] + p[3]
    else:
        p[0] = ""

def p_liczba(p):
    '''
    liczba : number_unsigned
        | minus number_unsigned
    '''
    if len(p) == 2:
        p[0] = str(p[1])
    else:
        p[0] = str(-p[2])

def p_wyr_w_naw(p):
    '''
    wyr_w_naw : l_parenthesis wyrazenie r_parenthesis
    '''
    p[0] = "(" + p[2] + ")"

def p_warunek(p):
    '''
    warunek : warunek_prosty
        | not warunek_prosty warunek_prostys
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = "not " + p[2] + p[3]

def p_warunek_prosty(p):
    '''
    warunek_prosty : wyrazenie oper_porownania wyrazenie
    '''
    p[0] = str(p[1]) + " " + p[2] + " " + str(p[3])

def p_warunek_prostys(p):
    '''
    warunek_prostys :
        | oper_war warunek_prosty
        | oper_war warunek_prosty warunek_prostys
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    elif len(p) == 4:
        p[0] = p[1] + p[2] + p[3]
    else:
        p[0] = ""

def p_oper_war(p):
    '''
    oper_war : and
        | or
    '''
    p[0] = p[1]

def p_oper_porownania(p):
    '''
    oper_porownania : equals
        | not_equals
        | greater
        | lower
        | greater_or_equal
        | lower_or_equal
    '''
    if p[1] == "đźŚ—":
        p[0] = "=="
    elif p[1] == "đźŚť":
        p[0] = ">"
    elif p[1] == "đźŚš":
        p[0] = "<"
    elif p[1] == "đźŚ’":
        p[0] = ">="
    elif p[1] == "đźŚ”":
        p[0] = "<="
    else:
        p[0] = p[1]

def p_not_equals(p):
    '''
    not_equals : not equals
    '''
    p[0] = "!" + "="

def p_for_warunek(p):
    '''
    for_warunek : instr_inicjuj warunek_prosty instr_podstaw
    '''
    minus = ""
    second = str(p[2]).split(" ")[-1]
    if str(p[3]).split(" ")[3] == "-":
        minus = "-"
    if str(p[2]).split(" ")[1] == "<=" or str(p[2]).split(" ")[1] == ">":
        second += " + 1"
    p[0] = str(p[1]).split(" ")[0] + " in " + "range(" + str(p[1]).split(" ")[-1] + ", " + str(second) + ", "+ minus + str(p[3]).split(" ")[-1] + ")"

def p_error(p):
    print("Syntax error in input!", p)
    global error
    error = True

parser = yacc.yacc()

with open(sys.argv[1]) as f:
    lines = f.readlines()

content = "".join(lines)

parser.parse(content)
import ply.yacc as yacc
from scanner import tokens

def p_start(p):
    'start : program'

def p_program(p):
    'program : blok'

def p_blok(p):
    '''
    blok : blok_deklaracji end blok_instrukcji end
        | end blok_instrukcji end
        | blok_deklaracji end end
        | end end
    '''

def p_blok_deklaracji(p):
    '''
    blok_deklaracji : dek_funs
    '''

def p_dek_funs(p):
    '''
    dek_funs :
        | dek_fun
        | dek_fun dek_funs
    '''

def p_dek_fun(p):
    '''
    dek_fun : function var_sym identifier l_parenthesis arguments r_parenthesis instrukcjas return wyrazenie end
        | function void identifier l_parenthesis arguments r_parenthesis instrukcjas return wyrazenie end
    '''

def p_arguments(p):
    '''
    arguments :
        | var_sym identifier
        | var_sym identifier arguments
    '''

def p_blok_instrukcji(p):
    '''
    blok_instrukcji : instrukcjas
    '''

def p_instrukcjas(p):
    '''
    instrukcjas :
        | instrukcja
        | instrukcja instrukcjas
    '''

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

def p_instr_inicjuj(p):
    '''
    instr_inicjuj : var_liczba_sym identifier assign liczba
        | var_liczba_sym identifier assign null
        | string identifier assign text
        | string identifier assign null
    '''

def p_instr_podstaw(p):
    '''
    instr_podstaw : identifier assign wyrazenie
        | identifier assign null
    '''

def p_instr_wywolaj(p):
    '''
    instr_wywolaj : call identifier l_parenthesis wyrazenies r_parenthesis
    '''

def p_wyrazenies(p):
    '''
    wyrazenies :
        | wyrazenie
        | wyrazenie wyrazenies
    '''

def p_instr_if(p):
    '''
    instr_if : if warunek then instrukcja instrukcjas
        | if warunek then instrukcja instrukcjas else instrukcja instrukcjas
    '''

def p_instr_while(p):
    '''
    instr_while : while warunek do instrukcjas
    '''

def p_instr_for(p):
    '''
    instr_for : for for_warunek do instrukcjas
    '''

def p_wypisz(p):
    '''
    wypisz : print wyrazenie
        | print text
    '''

def p_instr_switch(p):
    '''
    instr_switch : switch l_parenthesis wyrazenie r_parenthesis case_blok case_bloks case_default
    '''

def p_case_blok(p):
    '''
    case_blok : case l_parenthesis wyrazenie r_parenthesis then instrukcjas end
        | case l_parenthesis wyrazenie r_parenthesis then instrukcjas break end
    '''

def p_case_default(p):
    '''
    case_default : default then instrukcjas end
    '''

def p_case_bloks(p):
    '''
    case_bloks :
        | case_blok
        | case_blok case_bloks
    '''

def p_var_sym(p):
    '''
    var_sym : var_liczba_sym
        | string
        | boolean
        | char
    '''

def p_var_liczba_sym(p):
    '''
    var_liczba_sym : int
        | long
        | float
        | double
    '''

def p_wyrazenie(p):
    '''
    wyrazenie : skladnik skladniks
        | true
        | false
    '''

def p_skladnik(p):
    '''
    skladnik : czynnik czynniks
    '''


def p_skladniks(p):
    '''
    skladniks :
        | oper_add skladnik
        | oper_add skladnik skladniks
    '''

def p_oper_add(p):
    '''
    oper_add : plus
        | minus
    '''

def p_oper_mul(p):
    '''
    oper_mul : times
        | divide
    '''

def p_czynnik(p):
    '''
    czynnik : identifier
        | liczba
        | instr_wywolaj
        | wyr_w_naw
    '''

def p_czynniks(p):
    '''
    czynniks :
        | oper_mul czynnik
        | oper_mul czynnik czynniks
    '''

def p_liczba(p):
    '''
    liczba : number_unsigned
        | minus number_unsigned
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = -p[2]

def p_wyr_w_naw(p):
    '''
    wyr_w_naw : l_parenthesis wyrazenie r_parenthesis
    '''

def p_warunek(p):
    '''
    warunek : warunek_prosty warunek_prostys
        | not warunek_prosty warunek_prostys
    '''

def p_warunek_prosty(p):
    '''
    warunek_prosty : wyrazenie oper_porownania wyrazenie
    '''

def p_warunek_prostys(p):
    '''
    warunek_prostys :
        | oper_war warunek_prosty
        | oper_war warunek_prosty warunek_prostys
    '''

def p_oper_war(p):
    '''
    oper_war : and
        | or
    '''

def p_oper_porownania(p):
    '''
    oper_porownania : equals
        | not_equals
        | greater
        | lower
        | greater_or_equal
        | lower_or_equal
    '''

def p_not_equals(p):
    '''
    not_equals : not equals
    '''

def p_for_warunek(p):
    '''
    for_warunek : instr_inicjuj wyrazenie instr_podstaw
    '''

def p_error(p):
    print("Syntax error in input!", p)


parser = yacc.yacc()

with open('test2.txt') as f:
    lines = f.readlines()

content = "".join(lines)

parser.parse(content)
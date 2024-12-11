from ply import yacc
from lexer import tokens

def p_start(p):
    """start : eols STARTUML name EOL defs ENDUML eols"""
    pass

def p_eols(p):
    """eols : EOL eols
            | """
    pass

def p_name(p):
    """name : ID
            | """
    pass

def p_defs(p):
    """defs : one_def EOL
            | defs one_def EOL"""
    pass

def p_one_def(p):
    """one_def : ACTOR def_act alias stereo
               | ACTOR_TXT alias stereo
               | USECASE def_uc alias stereo
               | USE_CASE_TXT alias stereo
               | var arrow var ucl_link
               | var INHERIT var
               | PACKAGE ID LBRACE defs RBRACE"""
    pass

def p_stereo(p):
    """stereo : STEREO
              | """
    pass

def p_def_act(p):
    """def_act : ID
               | ACTOR_TXT
               | STRING"""
    pass

def p_ucl_link(p):
    """ucl_link : COLON EXTENDS
                | COLON INCLUDES
                | COLON ID
                | """
    pass

def p_arrow(p):
    """arrow : RIGHT_ARROW_1
             | RIGHT_ARROW_2"""
    pass

def p_var(p):
    """var : ID
           | USE_CASE_TXT
           | ACTOR_TXT"""
    pass

def p_alias(p):
    """alias : AS ID
             | """
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Unexpected end of input")

parser = yacc.yacc()
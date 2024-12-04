import ply.lex as lex

tokens = [
    'STARTUML',
    'ENDUML',
    'ACTOR',
    'AS',
    'USECASE',
    'PACKAGE',
    'INCLUDES',
    'EXTENDS',
    'COLON',
    'RIGHT_ARROW_1',
    'RIGHT_ARROW_2',
    'LBRACE',
    'RBRACE',
    'INHERIT',
    'EOL',
    'STRING',
    'STEREO',
    'ACTOR_TEXT',
    'USE_CASE_TEXT',
    'ID',
]

t_STARTUML = r'@startuml'
t_ENDUML = r'@enduml'
t_COLON = r':'
t_RIGHT_ARROW_1 = r'(-->|->)'
t_RIGHT_ARROW_2 = r'(\.\.>|\.>)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_INHERIT = r'<\|--'
t_STRING = r'"[^"]*"'
t_STEREO = r'<<[^>]+>>'
t_ACTOR_TEXT = r':[a-zA-Z0-9_ ]+:'
t_USE_CASE_TEXT = r'\([a-zA-Z0-9_ ]+\)'
t_EOL = r'\n+'
t_ignore = ' \t'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_error(t):
    print(f"Erreur lexicale : {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

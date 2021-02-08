import ply.lex as lex

class Lexer(object):
    # List of token names.   This is always required
    tokens = (
        'TEXT',
        'QUESTION',
        'PIPE',
        'COLON',
        'LDBRACE',
        'RDBRACE',
    )

    # Regular expression rules for simple tokens
    t_TEXT = r'[a-zA-Z !,]+'
    t_QUESTION = r'\?'
    t_PIPE = r'\|'
    t_COLON = r'\:'
    t_LDBRACE = r'\{\{'
    t_RDBRACE = r'\}\}'

    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

    # Error handling rule
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

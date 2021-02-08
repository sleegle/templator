import ply.yacc as yacc
from lexer import Lexer
import expr

class Parser(object):
    # Define lexer and tokens
    lexer = Lexer()
    tokens = Lexer.tokens

    def p_template(self, p):
        '''
        template : template expression
        '''
        p[0] = p[1].append(p[2])

    def p_template_empty(self, p):
        '''
        template : expression
        '''
        p[0] = expr.Sequence(p[1])

    def p_expression(self, p):
        '''
        expression : text
                   | variable
                   | condition
                   | switch
        '''
        p[0] = p[1]

    def p_text(self, p):
        '''
        text : TEXT
        '''
        p[0] = expr.Text(p[1].strip())

    def p_variable(self, p):
        '''
        variable : LDBRACE TEXT RDBRACE
        '''
        p[0] = expr.Variable(p[2].strip())
    
    def p_condition_left(self, p):
        '''
        condition : LDBRACE TEXT QUESTION template RDBRACE
        '''
        p[0] = expr.Condition(p[2].strip(), p[4])

    def p_condition(self, p):
        '''
        condition : LDBRACE TEXT QUESTION template PIPE template RDBRACE
        '''
        p[0] = expr.Condition(p[2].strip(), p[4], p[6])

    def p_switch(self, p):
        '''
        switch : LDBRACE TEXT QUESTION cases RDBRACE
        '''
        p[0] = expr.SwitchCase(p[2].strip(), p[4])

    def p_cases(self, p):
        '''
        cases : cases PIPE case 
        '''
        p[0] = p[1].append(p[3])

    def p_cases_case(self, p):
        '''
        cases : case
        '''
        p[0] = expr.Sequence(p[1])

    def p_case(self, p):
        '''
        case : TEXT COLON template
        '''
        p[0] = expr.Case(p[1].strip(), p[3])

    # Error rule for syntax errors
    def p_error(self, p):
        raise Exception("Syntax error in input!", p)

    # Build the parser
    def build(self, **kwargs):
        self.lexer.build()
        self.parser = yacc.yacc(module=self, start="template", **kwargs)

    def parse(self, data, **kwargs):
        return self.parser.parse(data)

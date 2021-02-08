class Expr:
    pass

class Text(Expr):
    def __init__(self, text):
        self.text = text

class Variable(Expr):
    def __init__(self, var):
        self.var = var
    
    def __str__(self):
        return "[" + self.var + "]"

class Condition(Expr):
    def __init__(self, condition, true, false=None):
        self.condition = condition
        self.true = true
        self.false = false
    
class Case(Expr):
    def __init__(self, key, value):
        self.key = key
        self.value = value

class SwitchCase(Expr):
    def __init__(self, switch, cases=None):
        self.switch = switch
        if cases is None:
            self.cases = ()
        else:
            self.cases = cases
    
    def keys(self):
        return list(map(lambda case: case.key, self.cases.items))
    
    def switchcase(self, case):
        for c in self.cases.items:
            if case == c.key:
                return c
        return None

class Sequence(Expr):
    def __init__(self, *items):
        if items is None:
            self.items = []
        else:
            self.items = list(items)

    def append(self, item):
        self.items.append(item)
        return self

import expr

class Evaluator(object):
    def __init__(self):
        self.switcher = {
            expr.Text: self.eval_text,
            expr.Variable: self.eval_variable,
            expr.Condition: self.eval_condition,
            expr.Case: self.eval_case,
            expr.SwitchCase: self.eval_switchcase,
            expr.Sequence: self.eval_sequence,
        }

    def eval_text(self, exp: expr.Text):
        pass

    def eval_variable(self, exp: expr.Variable):
        pass

    def eval_condition(self, exp: expr.Condition):
        pass

    def eval_switchcase(self, exp: expr.SwitchCase):
        pass

    def eval_case(self, exp: expr.Case):
        pass

    def eval_sequence(self, exp: expr.Sequence):
        pass

    def eval(self, exp: expr.Expr):
        pass

class FormEvaluator(Evaluator):
    def __init__(self):
        super().__init__()
        self.form = {}

    def eval_text(self, exp: expr.Text):
        pass

    def eval_variable(self, exp: expr.Variable):
        self.form[exp.var] = {
            'type': 'text',
        };

    def eval_condition(self, exp: expr.Condition):
        self.form[exp.condition] = {
            'type': 'bool',
        };
        self.eval(exp.true)
        self.eval(exp.false)

    def eval_switchcase(self, exp: expr.SwitchCase):
        keys = exp.keys() + list(self.form.get(exp.switch, {}).get('options', []))
        self.form[exp.switch] = {
            'type': 'select',
            'options': set(keys),
        };
        self.eval(exp.cases)

    def eval_case(self, exp: expr.Case):
        self.eval(exp.value)

    def eval_sequence(self, exp: expr.Sequence):
        list(map(self.eval, exp.items))

    def eval(self, exp: expr.Expr):
        self.switcher.get(exp.__class__, lambda: None)(exp)

class TextEvaluator(Evaluator):
    def __init__(self, form):
        super().__init__()
        self.form = form

    def eval_text(self, exp: expr.Text):
        return exp.text

    def eval_variable(self, exp: expr.Variable):
        return self.form.get(exp.var, None)

    def eval_condition(self, exp: expr.Condition):
        return self.eval(
            exp.true if self.form.get(exp.condition, True) else exp.false
        )

    def eval_switchcase(self, exp: expr.SwitchCase):
        return self.eval(exp.switchcase(self.form.get(exp.switch, None)))

    def eval_case(self, exp: expr.Case):
        return self.eval(exp.value)

    def eval_sequence(self, exp: expr.Sequence):
        return ' '.join(filter(lambda x: x is not None, map(self.eval, exp.items)))

    def eval(self, exp: expr.Expr):
        return self.switcher.get(exp.__class__, lambda x: None)(exp)

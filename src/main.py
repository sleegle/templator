from os import path, getcwd
from parser import Parser
from lexer import Lexer
import expr
from evaluator import FormEvaluator, TextEvaluator

p = Parser()
p.build()

inp = input('')

result = p.parse(inp)

form_evaluator = FormEvaluator()
form_evaluator.eval(result)
print("Form: ", form_evaluator.form)

form = {
    'name': "Ramtin",
    'gender': "male",
    'beard': False,
}
text_evaluator = TextEvaluator(form)
text = text_evaluator.eval(result)
print("Text", text)

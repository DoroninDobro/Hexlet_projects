from random import randint, choice
from operator import add, sub, mul

DESCRIPTION = 'What is the result of the expression?'


def round():
    x = randint(1, 99)
    y = randint(1, 99)
    list_operations = [('+', add), ('-', sub), ('*', mul)]
    operation, function = choice(list_operations)
    question = f'{x} {operation} {y}'
    correct = function(x, y)
    return question, str(correct)

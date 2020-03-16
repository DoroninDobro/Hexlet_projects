from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def round():
    question = randint(1, 99)
    if question % 2 == 0:
        correct = 'yes'
    else:
        correct = 'no'
    return str(question), correct

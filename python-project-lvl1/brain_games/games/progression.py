from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def round():
    start = randint(11, 100)
    step = randint(1, 25)
    ghost = randint(2, 9)
    question = str(start)
    for i in range(9):
        start += step
        if i != ghost - 1:
            question += ' ' + str(start)
        else:
            correct = str(start)
            question += ' ..'
    return question, correct

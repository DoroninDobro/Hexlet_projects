from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(x, y):
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return x+y


def round():
    x = randint(1, 100)
    y = randint(1, 100)
    correct = str(gcd(x, y))
    question = f'{str(x)} {str(y)}'
    return question, correct

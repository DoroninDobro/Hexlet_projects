from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    n = x - 1
    while x % n != 0:
        n -= 1
    if n == 1:
        return True
    return False


def round():
    x = randint(4, 550)
    correct = 'yes' if is_prime(x) else 'no'
    question = str(x)
    return question, correct

from brain_games import cli
import prompt


def run(game):
    score = 0
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    print('')
    name = cli.run()
    final_score = 3
    while score < final_score:
        question, correct = game.round()
        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if answer != correct:
            print(f"'{answer}' is wrong answer ;(. Correct answer "
                  f"was '{correct}'. Let's try again, {name}!")
            break
        score += 1
        print('Correct!')
    if score == final_score:
        print(f'Congratulations, {name}!')

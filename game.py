import time
import random
from util import clear


def run_game(game_data):
    score = 0
    for question_data in game_data:
        question = question_data['question']
        correct_answer = question_data['correct_answer']
        incorrect_answers = question_data['incorrect_answers']
        answers = incorrect_answers
        answers.append(correct_answer)
        random.shuffle(answers)

        print(question)
        for idx, answer in enumerate(answers):
            print(f'[{idx}] {answer}')

        user_choice = ""
        while user_choice == "":
            user_choice = input("\n>")
        print(f'Correct answer: {correct_answer}')
        time.sleep(2)
        clear()

        if answers[int(user_choice)] == correct_answer:
            score += 1

    print(f'You scored {score} out of {len(game_data)}')

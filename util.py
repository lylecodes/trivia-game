import os
import time


def prompt_user():
    print("Welcome to the trivia game!")
    print("You will be asked a series of questions that will help customize your experience!\n")
    time.sleep(3)

    # get number of questions
    num_questions = ""
    while num_questions == "":
        num_questions = input("How many questions would you like? [5-10]\n>")
    clear()

    # get category
    print("Choose one of the categories below:")
    categories = ['General Knowledge', 'Sports', 'History']
    for idx, category in enumerate(categories):
        print(f"[{idx}] {category}")
    category_choice = ""
    while category_choice == "":
        category_choice = input(">")
    clear()

    # get difficulty
    print("Choose a difficulty:")
    difficulties = ['Easy', 'Medium', 'Hard']
    for idx, difficulty in enumerate(difficulties):
        print(f"[{idx}] {difficulty}")
    difficulty_choice = ""
    while difficulty_choice == "":
        difficulty_choice = input(">")
    clear()

    print("Select a type:")
    quiz_types = ['Multiple Choice', 'True/False']
    for idx, quiz_type in enumerate(quiz_types):
        print(f'[{idx}] {quiz_type}')
    type_choice = ""
    while type_choice == "":
        type_choice = input(">")
    clear()

    print("Building game...")

    return {'num_questions': num_questions,
            "category_choice": category_choice,
            "difficulty_choice": difficulty_choice,
            "type_choice": type_choice}


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

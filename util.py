import os
import time


def prompt_user():
    print("Welcome to the trivia game!")
    print("You will be asked a series of questions that will help customize your experience!\n")
    time.sleep(3.5)
    clear()

    # get number of questions
    num_questions = ""
    while num_questions == "":
        num_questions = input("How many questions would you like? [5-10]\n\n>")
    clear()

    # get category
    print("Choose one of the categories below:")
    categories = ['General Knowledge', 'Sports', 'History']
    category_dict = {'0': 9, '1': 21, '2': 23}
    for idx, category in enumerate(categories):
        print(f"[{idx}] {category}")
    category_choice = ""
    while category_choice == "":
        category_choice = input("\n>")
    category = category_dict[category_choice]
    clear()

    # get difficulty
    print("Choose a difficulty:")
    difficulties = ['Easy', 'Medium', 'Hard']
    for idx, difficulty in enumerate(difficulties):
        print(f"[{idx}] {difficulty}")
    difficulty_choice = ""
    while difficulty_choice == "":
        difficulty_choice = input("\n>")
    difficulty = difficulties[int(difficulty_choice)]
    clear()

    print("Select a type:")
    quiz_types = ['Multiple Choice', 'True/False']
    for idx, quiz_type in enumerate(quiz_types):
        print(f'[{idx}] {quiz_type}')
    type_choice = ""
    while type_choice == "":
        type_choice = input("\n>")
    if type_choice == '0':
        type_choice = 'multiple'
    elif type_choice == '1':
        type_choice = 'boolean'
    clear()

    print("Building game...")

    return {'num_questions': num_questions,
            "category": category_choice,
            "difficulty": difficulty_choice,
            "type_choice": type_choice}


def clear():
    os.system('cls')

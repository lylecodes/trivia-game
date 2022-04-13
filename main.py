from util import prompt_user
from data import fetch_question_data
from game import run_game


def main():
    user_input_data = prompt_user()
    game_data = fetch_question_data(user_input_data)
    run_game(game_data)


if __name__ == '__main__':
    main()

import requests


def fetch_question_data(user_input):
    num_questions = user_input['num_questions']
    category = user_input['category']
    difficulty = user_input['difficulty']
    quiz_type = user_input['type_choice']

    url = f'https://opentdb.com/api.php?amount={num_questions}&category={category}&difficulty={difficulty}&type={quiz_type}'
    res = requests.get(url).json()
    return format_data(res)


def format_data(res):
    data = []

    for x in res['results']:
        q_dict = {'question': x['question'], 'correct_answer': x['correct_answer'],
                  'incorrect_answers': x['incorrect_answers']}
        data.append(q_dict)

    return data

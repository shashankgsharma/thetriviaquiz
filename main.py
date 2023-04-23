from questionModel import Question
from quizBrain import SelectLevel, CalculateScore, SelectMode
from os import system
from random import sample


def clear():
    system('cls')


play_again = True
while play_again:
    clear()
    print("Welcome to The Trivia QUIZ!")
    user_score = 0
    user_mode = input("Choose Game Mode: IPL mode(i)/ MOVIES mode(m)/ Computer Science(CS) mode(c): [Default mode is "
                      "IPL] ")
    data, game_mode = SelectMode(user_mode).select_data()

    object_list = []
    for q_no in data.keys():
        obj_fact = data[q_no]["fact"]
        obj_value = data[q_no]["value"]
        object_list.append(Question(obj_fact, obj_value))

    random_object_list = sample(object_list, len(object_list))
    level = input("Choose a level: easy(e)-10Q, medium(m)-20Q, hard(h)-30Q, pro(p)-50Q: ")
    num_q, game_difficulty = SelectLevel(level).count_q()
    clear()
    print(f"\nGame Mode: {game_mode}")
    print(f"Difficulty Level: {game_difficulty}")
    print(f"Total Questions: {num_q}\n")
    for i in range(num_q):
        user_in = input(f"Q{i + 1}. " + random_object_list[i].fact + ": (True/ False)?\n")
        user_score = CalculateScore(user_in, random_object_list, i, user_score).calculate()
        print(f"User's Score: ({user_score}/{i + 1}).\n")
    print(f"You've Completed the quiz.\nYour Final Score is: ({user_score}/{num_q}).")
    if input("Wanna play again? Yes(y)/ No(n)?: ").lower() == 'n':
        play_again = False
        clear()
        print("Goodbye!")

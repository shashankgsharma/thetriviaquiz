import os
from data import ipl_data, cs_data, movies_data


class SelectLevel:
    def __init__(self, level):
        self.level = level

    def count_q(self):
        if self.level.lower() == 'e' or self.level.lower() == 'easy':
            return 10, "Easy"
        elif self.level.lower() == 'm' or self.level.lower() == 'medium':
            return 20, "Medium"
        elif self.level.lower() == 'h' or self.level.lower() == 'hard':
            return 30, "Hard"
        elif self.level.lower() == 'p' or self.level.lower() == 'pro':
            return 50, "Pro"
        else:
            return 5, "Default"


class CalculateScore:
    def __init__(self, user_in, object_list, i, user_score):
        self.user_in = user_in
        self.object_list = object_list
        self.i = i
        self.user_score = user_score

    def calculate(self):
        if self.user_in.lower() == 'true' or self.user_in.lower() == 't':
            user_in_bool = True
        elif self.user_in.lower() == 'false' or self.user_in.lower() == 'f':
            user_in_bool = False
        elif self.user_in.lower() == 'exit':
            user_in_bool = 'end'
        else:
            user_in_bool = 'invalid'

        if user_in_bool == self.object_list[self.i].value:
            self.user_score += 1
            print("You're right!")
        elif user_in_bool == 'end':
            play_again = False
            os.system('cls')
            print('Goodbye')
            exit()
        elif user_in_bool == 'invalid':
            print("Invalid Input!")
        else:
            print("You're wrong.")
        return self.user_score


class SelectMode:
    def __init__(self, mode):
        self.mode = mode

    def select_data(self):
        if self.mode.lower() == 'cs' or self.mode.lower() == 'c':
            return cs_data, "Computer Science"
        elif self.mode.lower() == 'movies' or self.mode.lower() == 'm':
            return movies_data, "Movies"
        else:
            return ipl_data, "Indian Premier League"

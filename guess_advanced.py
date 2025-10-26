import random
from datetime import datetime

GREETINGS = """Привет! Давай поиграем? Я загадываю число, а
ты пытаешься его угадать за определенное число попыток. Если тебе
не удастся отгадать число, то ты проиграешь, если получится, ты победишь и я тебя похвалю(нет).
Согласен? Для начала выбери уровень сложности, просто поставь цифру ниже:
"""
GREETINGS_EASY_DIFFICULTY_CHOOSE = "1 - Легкий: от 1 до 50. 10 попыток"
GREETINGS_MEDIUM_DIFFICULTY_CHOOSE = "2 - Средний: от 1 до 100. 7 попыток"
GREETINGS_HARD_DIFFICULTY_CHOOSE = "3 - Сложный: от 1 до 1000. 10 попыток"
win_or_lose = "" 

def func_game_greetings():

    print(GREETINGS)
    print(GREETINGS_EASY_DIFFICULTY_CHOOSE)
    print(GREETINGS_MEDIUM_DIFFICULTY_CHOOSE)
    print(GREETINGS_HARD_DIFFICULTY_CHOOSE)


def main():

    user_choice_of_difficulty = func_validation_choice_difficulty()


    min_possible_number, max_possible_number = func_choose_difficulty(user_choice_of_difficulty)
    attempts = func_calculating_number_of_attempts(user_choice_of_difficulty)
    computer_random_number = func_computer_deciding_number(min_possible_number,max_possible_number)


    func_game_start(attempts, computer_random_number, min_possible_number, max_possible_number)


def func_game_start(attempts, computer_random_number, min_possible_number, max_possible_number):

    while True:

        print("Твои догадки?")

        player_guess = func_player_guess_validation(min_possible_number, max_possible_number)


        if computer_random_number > player_guess:
            print("Мое число больше")

        elif computer_random_number < player_guess:
            print("Мое число меньше твоего")

        else:
            print(f"Ты угадал! Мое число {computer_random_number}")
            return func_game_restart()
        
        if attempts == 0:
            print("Кажется все твои попытки кончились. Как жаль")
            return func_game_restart()
        
        attempts = attempts - 1
        print(f"Число попыток: {attempts}")


def func_validation_choice_difficulty():

    available_difficulty_options = [1,3]

    while True:

        try:

            user_choice_of_difficulty = input()

            user_choice_of_difficulty.strip() 
            #нашел функцию которая удаляет пробелы из строк

            user_choice_of_difficulty.strip("-").isdigit() 
            #проверка на то, число ли строка введеная пользователем

            user_choice_of_difficulty = int(user_choice_of_difficulty)
            #если да, то строка становится числом и после проверяется

            if user_choice_of_difficulty in available_difficulty_options:
                    return user_choice_of_difficulty    
            print("Число больше или меньше")

        except ValueError:

            print(f"Похоже что ты ввел букву или символ либо же вообще ничего. Введи число от {available_difficulty_options}")


def func_choose_difficulty(user_choice_of_difficulty): 
    
    max_possible_number = user_choice_of_difficulty
    min_possible_number = 1

    match max_possible_number:
        #Минимальное возможные границы для числа! Теперь с ними можно экспериментировать как угодно
        case 1:
            min_possible_number = 1
            max_possible_number = 50

        case 2:
            min_possible_number = 1
            max_possible_number = 100

        case 3:
            min_possible_number = 1
            max_possible_number = 1000

    return min_possible_number,max_possible_number


def func_calculating_number_of_attempts(user_choice_of_difficulty):

    attempts = 10
    attempts_depending_on_difficulty = user_choice_of_difficulty

    match attempts_depending_on_difficulty:

        case 1: 
            attempts = 10

        case 2:
            attempts = 7

        case 3:
            attempts = 10

    return attempts


def func_computer_deciding_number(min_possible_number, max_possible_number):

    min_possible_computer_number = min_possible_number
    max_possible_computer_number = max_possible_number
    
    computer_random_number = random.randint(min_possible_computer_number, max_possible_computer_number)

    return computer_random_number


def func_player_guess_validation(min_possible_number, max_possible_number):

    while True:

        try:

            player_guess = input()

            player_guess.strip()
            player_guess.strip("-").isdigit()
            player_guess = int(player_guess)

            if min_possible_number <= player_guess <= max_possible_number:
                return player_guess
            print(f"Я чувствую что твое число выходит за рамки от {min_possible_number} до {max_possible_number}")

        except ValueError:

            print(f"Введи число от {min_possible_number} до {max_possible_number}")


def func_game_restart():

    do_restart = input("Хочешь сыграть ещё раз? (да/нет): ")

    if do_restart == "да":
        print("Выбирай тогда сложность")
        main()

    else:
        print("Оки, было весело")    

func_game_greetings()
main()
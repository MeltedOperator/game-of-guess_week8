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

#подумываю над тем, как можно упростить функции о валидации, попытках и выборе сложности
def func_game_greetings():

    print(GREETINGS)
    print(GREETINGS_EASY_DIFFICULTY_CHOOSE)
    print(GREETINGS_MEDIUM_DIFFICULTY_CHOOSE)
    print(GREETINGS_HARD_DIFFICULTY_CHOOSE)

    return 0


def main():

    user_choice_of_difficulty = func_validation_choice_difficulty()


    min_possible_number_border, max_possible_number_border = func_choose_difficulty(user_choice_of_difficulty)

    attempts = func_calculating_number_of_attempts(user_choice_of_difficulty)

    computer_random_number = func_computer_deciding_number(min_possible_number_border,max_possible_number_border)

    func_game_start(attempts, computer_random_number, min_possible_number_border, max_possible_number_border)


def func_game_start(attempts, computer_random_number, min_possible_number_border, max_possible_number_border):

    while True:

        player_guess = func_player_guess_validation(min_possible_number_border, max_possible_number_border)


        if computer_random_number > player_guess:
            print("Мое число больше")

        elif computer_random_number < player_guess:
            print("Мое число меньше твоего")

        else:
            print(f"Ты угадал! Мое число {computer_random_number}")
            return func_game_restart()
        
        if attempts == 0:
            print("Кажется все твои попытки кончились. Как жаль")
            return func_game_restart
        
        attempts = attempts - 1
        print(f"Число попыток: {attempts}")


def func_validation_choice_difficulty():
    while True:
        try:
            user_choice_of_difficulty = int(input())
            if 0 < user_choice_of_difficulty < 4:
                    return user_choice_of_difficulty
            print("Число больше или меньше")
        except ValueError:
            print("Похоже что ты ввел букву или символ, а не число, либо же вообще ничего. Введи число от 1 до 3")


def func_choose_difficulty(user_choice_of_difficulty): 
    
    max_possible_number_border = user_choice_of_difficulty
    min_possible_number_border = 1

    match max_possible_number_border:
        #Минимальное возможные границы для числа! Теперь с ними можно экспериментировать как угодно
        case 1:
            min_possible_number_border = 1
            max_possible_number_border = 50

        case 2:
            min_possible_number_border = 1
            max_possible_number_border = 100

        case 3:
            min_possible_number_border = 1
            max_possible_number_border = 1000


    return min_possible_number_border,max_possible_number_border


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


def func_computer_deciding_number(min_possible_number_border, max_possible_number_border):

    min_possible_computer_number = min_possible_number_border
    max_possible_computer_number = max_possible_number_border
    
    computer_random_number = random.randint(min_possible_computer_number, max_possible_computer_number)

    return computer_random_number


def func_player_guess_validation(min_possible_border_number, max_possible_number_border):
    while True:
        try:
            player_guess = int(input())
            if min_possible_border_number <= player_guess <= max_possible_number_border:
                return player_guess
            print(f"Я чувствую что твое число выходит за рамки от {min_possible_border_number} до {max_possible_number_border}")

        except ValueError:
            print(f"Введи число от {min_possible_border_number} до {max_possible_number_border}")


def func_game_restart():

    do_restart = input("Хочешь сыграть ещё раз? (да/нет): ")

    if do_restart == "да":
        print("Выбирай тогда сложность")
        main()

    else:
        print("Оки, было весело")    


# def func_savestats(attempts_results, start_attempts_results, difficulty_results, endgame_state): 
    
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     GAME_OVER_STATS = f"""Игра была: {endgame_state} | {timestamp} 
#     | Осталось попыток: {attempts_results}
#         из {start_attempts_results} возможных | Сложность игры: {difficulty_results}"""
    
#     with open("stats2.txt", "a", encoding="utf-8") as f:
#         f.write(GAME_OVER_STATS)

func_game_greetings()
main()

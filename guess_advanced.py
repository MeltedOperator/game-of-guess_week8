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

def main():
    user_choice_of_difficulty = int(input())
    max_possible_number_border = func_choose_difficulty(user_choice_of_difficulty)

    attempts = func_calculating_number_of_attempts(user_choice_of_difficulty)
    computer_random_number = func_computer_deciding_number(max_possible_number_border)
    print(computer_random_number, attempts)

    # while True:

    #     attempts -= 1
    #     #guess = func_player_guess_validation(max_possible_number_border=max_possible_number_border, prompt=f"Твоя догадка? ", player_guess=0) #наше предположение

    #     if computer_random_number > guess:
    #         print("Моё число больше твоего")

    #     elif computer_random_number < guess:
    #         print("Моё число меньше твоего")

    #     else:
    #         print(f"Ты угадал! Моё число было {computer_random_number}")
    #         win_or_lose = "Выиграна"
    #         break

    #     if attempts == 0:
    #         print("Кажется у тебя закончились попытки, ты проиграл!")
    #         win_or_lose = "Проиграна"
    #         break

    #     print(f"Оставшиеся попытки: {attempts}")
             
    # func_savestats(attempts,start_number_attempts, difficulty, win_or_lose)
    # func_game_restart() 


def func_choose_difficulty(user_choice_of_difficulty): 
    
    max_possible_number_border = user_choice_of_difficulty

    match max_possible_number_border:

        case 1:
            max_possible_number_border = 50

        case 2:
            max_possible_number_border = 100

        case 3:
            max_possible_number_border = 1000


    return max_possible_number_border


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


def func_computer_deciding_number(max_possible_number_border):

    max_possible_computer_number = max_possible_number_border
    
    computer_random_number = random.randint(1, max_possible_computer_number)

    return computer_random_number


def func_player_guess_validation(prompt, player_guess, max_possible_number_border): #валидация ввода игроком числа. Оно не может быть меньше 1 и больше верхней границы
    
    while True:
        try:

            player_guess = int(input(prompt))

            if 1 <= player_guess <= max_possible_number_border:
                return player_guess
            print(f"Я чувствую что твое число выходит за рамки от 1 до {max_possible_number_border}")

        except ValueError:
            print("это даже не число...")


def func_savestats(attempts_results, start_attempts_results, difficulty_results, endgame_state): 
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    GAME_OVER_STATS = f"""Игра была: {endgame_state} | {timestamp} 
    | Осталось попыток: {attempts_results}
        из {start_attempts_results} возможных | Сложность игры: {difficulty_results}"""
    
    with open("stats2.txt", "a", encoding="utf-8") as f:
        f.write(GAME_OVER_STATS)


def func_game_greetings():

    print(GREETINGS)
    print(GREETINGS_EASY_DIFFICULTY_CHOOSE)
    print(GREETINGS_MEDIUM_DIFFICULTY_CHOOSE)
    print(GREETINGS_HARD_DIFFICULTY_CHOOSE)

    return 0


def func_game_restart():

    do_restart = input("Хочешь сыграть ещё раз? (да/нет): ")

    if do_restart == "да":
        print("Выбирай тогда сложность")
        main()

    else:
        print("Оки, было весело")

func_game_greetings()
main()

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

def game_greetings():

    print(GREETINGS)
    print(GREETINGS_EASY_DIFFICULTY_CHOOSE)
    print(GREETINGS_MEDIUM_DIFFICULTY_CHOOSE)
    print(GREETINGS_HARD_DIFFICULTY_CHOOSE)


def main():

    user_choice_of_difficulty = validation_choice_difficulty()


    min_possible_number, max_possible_number = choose_difficulty(user_choice_of_difficulty)
    attempts, difficulty = calculating_number_of_attempts(user_choice_of_difficulty)
    computer_random_number = computer_deciding_number(min_possible_number,max_possible_number)
    result = game_start(attempts, computer_random_number, min_possible_number, max_possible_number)


    endgame_stats(result, attempts, computer_random_number,difficulty)


def game_start(attempts, computer_random_number, min_possible_number, max_possible_number):

    while True:

        player_guess = player_guess_validation(min_possible_number, max_possible_number)

        attempts = attempts - 1

        if computer_random_number > player_guess:
            print("Мое число больше")

        elif computer_random_number < player_guess:
            print("Мое число меньше твоего")

        else:
            print(f"Ты угадал! Мое число {computer_random_number}")
            win_or_lose = "win"
            break

        if attempts == 0:
            print("Кажется все твои попытки кончились. Как жаль")
            win_or_lose = "lose"
            break
        
        print(f"Число попыток: {attempts}") 

    return win_or_lose

def removing_backspace(player_input):

    player_input.strip()
    player_input.strip("-").isdigit() 
    player_input = int(player_input)
    return player_input


def validation_choice_difficulty():

    available_difficulty_options = [1,2,3]
    options = (', '.join(map(str,available_difficulty_options)))

    while True:

        try:

            player_input = input()
            user_choice_of_difficulty = removing_backspace(player_input)

            if user_choice_of_difficulty in available_difficulty_options:
                    return user_choice_of_difficulty    
            
            print("Твое число больше 3 или меньше 1")

        except ValueError:
            print("Введи любое из следующих чисел:", options)


def choose_difficulty(user_choice_of_difficulty): 
    
    max_possible_number = user_choice_of_difficulty
    min_possible_number = 1

    match max_possible_number:

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


def calculating_number_of_attempts(user_choice_of_difficulty):

    attempts = 10
    attempts_depending_on_difficulty = user_choice_of_difficulty

    match attempts_depending_on_difficulty:

        case 1: 
            attempts = 10
            difficulty = "легкая сложность"

        case 2:
            attempts = 7
            difficulty = "средняя сложность"

        case 3:
            attempts = 10
            difficulty = "сложная сложность"

    return attempts, difficulty


def computer_deciding_number(min_possible_number, max_possible_number):

    min_possible_computer_number = min_possible_number
    max_possible_computer_number = max_possible_number
    
    computer_random_number = random.randint(min_possible_computer_number, max_possible_computer_number)

    return computer_random_number


def player_guess_validation(min_possible_number, max_possible_number):

    while True:

        try:
            player_input = input("Твои догадки? ")

            player_guess = removing_backspace(player_input)

            if min_possible_number <= player_guess <= max_possible_number:
                return player_guess
            print(f"Твое число выходит за рамки от {min_possible_number} до {max_possible_number}!")

        except ValueError:

            print(f"Введи число от {min_possible_number} до {max_possible_number}")


def game_restart():

    agreement = ["да", "д"]
    disagreement = ["нет", "н"]

    while True:

        do_restart = input("Хочешь сыграть ещё раз? Скажи да или нет: ")

        if do_restart.strip() in agreement:
            print("Выбирай тогда сложность")
            main()

        elif do_restart.strip() in disagreement:
            print("Оки, было весело")    
            return None


def endgame_stats(result, attempts, computer_random_number,difficulty):

    with open("stats.txt", "a") as f:

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"""время игры: {timestamp} | игра была: {result} |оставшиеся попытки: {attempts} | 
        загаданное число: {computer_random_number} | сложность игры: {difficulty} |""")

game_greetings()
main()
game_restart()
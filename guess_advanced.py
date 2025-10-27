import random
from datetime import datetime
import os

GREETINGS = """Привет! Давай поиграем? Я загадываю число, а
ты пытаешься его угадать за определенное число попыток. Если тебе
не удастся отгадать число, то ты проиграешь, если получится, ты победишь и я тебя похвалю(нет).
Согласен? Для начала выбери уровень сложности, просто поставь цифру ниже:
"""
GREETINGS_EASY_DIFFICULTY_CHOOSE = "1 - Легкий: от 1 до 50. 10 попыток"
GREETINGS_MEDIUM_DIFFICULTY_CHOOSE = "2 - Средний: от 1 до 100. 7 попыток"
GREETINGS_HARD_DIFFICULTY_CHOOSE = "3 - Сложный: от 1 до 1000. 10 попыток"

CURRENT_TURN = 1
attempts = 10

def game_greetings():

    """функция которая приветствует пользователя и предлагает ему выбрать
    одну из предложенных сложностей"""

    print(GREETINGS)
    print(GREETINGS_EASY_DIFFICULTY_CHOOSE)
    print(GREETINGS_MEDIUM_DIFFICULTY_CHOOSE)
    print(GREETINGS_HARD_DIFFICULTY_CHOOSE)


def main():
    user_choice_of_difficulty = validation_choice_difficulty()

    min_possible_number, max_possible_number = choose_difficulty(user_choice_of_difficulty)
    attempts, difficulty = calculating_number_of_attempts(user_choice_of_difficulty)
    computer_random_number = computer_deciding_number(min_possible_number,max_possible_number)

    print(f"была выбрана {difficulty}")

    result, aftermath_attempts = game_start(attempts, computer_random_number, min_possible_number, max_possible_number)

    print(endgame_stats(result, aftermath_attempts, computer_random_number, difficulty))
    game_restart()


def game_start(attempts, computer_random_number, min_possible_number,max_possible_number):

    """эта функция начинает игру:
    1)player_guess - спрашивает у пользователя число - догадку
    2)с каждым ходом число попыток уменьшается. С каждой итерацией игрок ближе к выигрышу или проигрышу
    3)CURRENT_GAME - переменная, которая показывает текущее состояние игры. Пока число попыток не равно нулю и/или игрок
    не угадал число, загаданное компьютером, то компьютер дает подсказки(см. в giving_hints)
    4)возвращает итог игры и число оставшихся попыток"""

    while True:

        player_guess = player_guess_validation(min_possible_number,max_possible_number)
        attempts = attempts - CURRENT_TURN
 
        CURRENT_GAME = giving_hints(player_guess, computer_random_number, attempts)
         
        print(f"Число попыток оставшихся: {attempts}") 

        if CURRENT_GAME != "в процессе":
            break

    return CURRENT_GAME, attempts


def giving_hints(player_guess, computer_random_number, attempts):

    """Функция подсказывает игроку и говорит, меньше или же больше задуманное компьютером число.
    Если игра заканчивается, то возвращает один из результатов - CURRENT_GAME выиграна или проиграна"""

    CURRENT_GAME = "в процессе"

    if computer_random_number > player_guess:
        print("Мое число больше твоего")

    elif computer_random_number < player_guess:
        print("Мое число меньше твоего")

    else:
        print(f"Ты угадал! Мое число {computer_random_number}")
        CURRENT_GAME = "выиграна"
        return CURRENT_GAME
    
    if attempts == 0:
        print("Кажется все твои попытки кончились. Как жаль")
        CURRENT_GAME = "проиграна"

    return CURRENT_GAME


def validation_choice_difficulty():

    """Валидация выбора сложности. Игроку дается выбор из available_difficulty_options.
    OPTIONS - это набор допустимых вариантов без скобок и запятых. До тех пор, пока игрок
    не выбрал одну из возможных сложностей(в текущей версии от 1 до 3) валидация кода будет
    продолжаться и код не перейдет к следующей функции. Функция работает даже если введена
    буква, число больше или меньше допустимого значения. Если в вводе
    есть пробелы - то они убираются благодаря функции removing_backspace_from_input"""

    available_difficulty_options = [1,2,3]
    OPTIONS = (', '.join(map(str,available_difficulty_options))) #убираем квадратные скобки и запятые

    while True:
        try:
            player_input = input()
            user_choice_of_difficulty = removing_backspace_from_input(player_input)

            if user_choice_of_difficulty in available_difficulty_options:
                    return user_choice_of_difficulty    
            print(f"Твое число меньше {OPTIONS[0]} или больше {OPTIONS[-1]}. Выбери из промежутка")

        except ValueError:
            print("Введи любое из следующих чисел:", OPTIONS)


def choose_difficulty(user_choice_of_difficulty): 

    """после проверки ввода в validation_choice_difficulty() запрос обрабатывается
    и в зависимости от выбранной сложности выбираются минимальные(min_possible_number) 
    и максимальные(max_possible_number) рамки для возможного числа, как для компьютера
    так и для пользователя, сохраненные настройки после будут использоваться в 
    других функциях для загадывания компьютером числа и последующей валидации числа пользователя"""

    max_possible_number = user_choice_of_difficulty
    min_possible_number = user_choice_of_difficulty

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

    """Функция в зависимости от сложности определяет количество попыток(attempts), за которые игрок
    должен угадать загаданное компьютером число. Здесь же определяется сложность игры(DIFFICULTY)
    чтобы после ее записать в итоги игры и в отдельный файл формата .txt (stats.txt)"""

    attempts_depending_on_difficulty = user_choice_of_difficulty 

    match attempts_depending_on_difficulty: 
        case 1: 
            attempts = 10
            DIFFICULTY = "легкая сложность"

        case 2:
            attempts = 7
            DIFFICULTY = "средняя сложность"

        case 3:
            attempts = 10
            DIFFICULTY = "сложная сложность"

    return attempts, DIFFICULTY


def computer_deciding_number(min_possible_number, max_possible_number):

    """В этой функции компьютер загадывает число(computer_random_number) не заходя за 
    установленные раннее рамки(min_possible_number, max_possible_number)"""

    computer_random_number = random.randint(min_possible_number, max_possible_number)

    return computer_random_number


def player_guess_validation(min_possible_number, max_possible_number):

    """В этой функции ввод игрока обрабатывается, и если введенное им число 
    не выходит за рамки(min_possible_number, max_possible_number) то после
    возвращается для использования в функции game_start(). Если ввод неправильный - 
    то цикл продолжается, принуждая игрока ввести число по всем правилам. Если в вводе
    есть пробелы - то они убираются благодаря функции removing_backspace_from_input"""

    while True:
        try:
            player_input = input("Твои догадки? ")

            player_guess = removing_backspace_from_input(player_input)

            if min_possible_number <= player_guess <= max_possible_number:
                return player_guess
            print(f"Твое число выходит за рамки от {min_possible_number} до {max_possible_number}!")

        except ValueError:

            print(f"Введи число от {min_possible_number} до {max_possible_number}")


def removing_backspace_from_input(player_input):

    """Функция принимает запрос пользователя, после чего сначала удаляет из него
    все пустые пространства( player_input.strip() ), затем, полученная строка 
    превращается в число(int) и возвращает значение, которое уже после обрабатывают
    player_guess_validation() и validation_choice_difficulty()"""

    player_input.strip("-").isdigit() 
    player_input = int(player_input)

    return player_input


def endgame_stats(current_game, aftermath_attempts, computer_random_number,difficulty):

    """В этой функции все результаты(SAVED_STATS) записываются в отдельный текстовый файл(stats.txt)
    для их последующего хранения, все остальные результаты удаляются после закрытия
    программы. current_game - итоги игры(была ли она выиграна или проиграна)
    aftermath_attempts - выводятся оставшиеся попытки
    computer_random_number - число, загаданное компьютером
    difficulty - выбранная игроком сложность. Все эти переменные записываются в SHOWN_STATS
    и показываются в консоли, а после SAVED_STATS остается в текстовом файле, для дальнейшей обработки"""

    TIMESTAMP = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    SHOWN_STATS = (f"""время игры: {TIMESTAMP} | игра была: {current_game} |оставшиеся попытки: {aftermath_attempts} | 
    загаданное число: {computer_random_number} | сложность игры: {difficulty} |""")

    SAVED_STATS = SHOWN_STATS

    with open("stats.txt", "a", encoding="utf-8") as f:
        f.write(SAVED_STATS + "\n")

    return SHOWN_STATS


def game_restart():

    """Функция запускает main() если игрок желает повторной игры. списки 
    agreement и disagreement используются для проверки ввода пользователя.
    Если он соглашается - игра продолжается. Если нет - игра заканчивается"""

    agreement = ["да", "д"]
    disagreement = ["нет", "н"]

    while True:
        do_restart = input("Хочешь сыграть ещё раз? Скажи да или нет: ")

        if do_restart.strip() in agreement:
            print("Выбирай тогда сложность")
            main()

        elif do_restart.strip() in disagreement:
            print("Удачи, было весело")    
            return None
        
game_greetings()
main()

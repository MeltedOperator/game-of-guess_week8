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
attempts = 10
win_or_lose = "" 
difficulty = "" 

def main(attempts):
    max_possible_number_border = int(func_choose_difficulty()) 

    if max_possible_number_border <= 50: 
        difficulty = "Легкая"

    elif 50 < max_possible_number_border <= 100:
        attempts = 7
        difficulty = "Средняя"

    else:
        difficulty = "Сложная"

    start_number_attempts = attempts #количество попыток, которое было вначале(тоже для статистики)
    computer_random_number = random.randint(1, max_possible_number_border) #число компьютера
    
    while True:

        attempts -= 1
        answer = func_player_guess_validation(max_possible_number_border=max_possible_number_border, prompt=f"Твоя догадка? ", player_guess=0) #наше предположение

        if computer_random_number > answer:
            print("Моё число больше твоего")

        elif computer_random_number < answer:
            print("Моё число меньше твоего")

        else:
            print(f"Ты угадал! Моё число было {computer_random_number}")
            win_or_lose = "Выиграна"
            break

        if attempts == 0:
            print("Кажется у тебя закончились попытки, ты проиграл!")
            win_or_lose = "Проиграна"
            break

        print(f"Оставшиеся попытки: {attempts}")

    func_savestats(attempts,start_number_attempts, difficulty, win_or_lose)
    func_game_restart() 


def func_game_restart(): #рестарт игры

    do_restart = input("Хочешь сыграть ещё раз? (да/нет): ")

    if do_restart == "да":
        print("Выбирай тогда сложность")
        main(attempts)

    else:
        print("Оки, было весело")

def func_player_guess_validation(prompt, player_guess, max_possible_number_border): #валидация ввода игроком числа. Оно не может быть меньше 1 и больше верхней границы
    
    while True:
        try:

            player_guess = int(input(prompt))

            if 1 <= player_guess <= max_possible_number_border:
                return player_guess
            print(f"Я чувствую что твое число выходит за рамки от 1 до {max_possible_number_border}")

        except ValueError:
            print("это даже не число...")

def func_choose_difficulty(): #игрок здесь выбирает сложность. Тут тоже смотрим чтобы он ввел правильное значение
    
    while True:
        try:

            user_skill = int(input()) 
            if user_skill == 1:
                print("Легкая сложность")
                return 50
            
            elif user_skill == 2:
                print("Средняя сложность")
                return 100
            
            elif user_skill == 3:
                print("Сложная сложность")
                return 1000
            
            else:
                print("Такой сложности нет, попробуй снова.")
   
        except ValueError:
            print("это даже не число")

print(GREETINGS)
print(GREETINGS_EASY_DIFFICULTY_CHOOSE)
print(GREETINGS_MEDIUM_DIFFICULTY_CHOOSE)
print(GREETINGS_HARD_DIFFICULTY_CHOOSE)

def func_savestats(attempts_results, start_attempts_results, difficulty_results, endgame_state): 
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    GAME_OVER_STATS = f"""Игра была: {endgame_state} | {timestamp} 
    | Осталось попыток: {attempts_results}
        из {start_attempts_results} возможных | Сложность игры: {difficulty_results}"""
    
    with open("stats2.txt", "w", encoding="utf-8") as f:
        f.write(GAME_OVER_STATS)
        
main(attempts)
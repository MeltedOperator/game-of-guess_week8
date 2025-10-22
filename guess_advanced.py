#alright, we have a working code and i can already see many issues, for as such - too many lines of code in main function, and magic numbers
import random
from datetime import datetime

def main():

    max_value = int(difficulty_choose()) #для рандомного числа ставим верхнюю границу исходя из сложности
    attempts = 10
    endgame_state = "" #здесь определим окончание игры(победа или поражение)
    difficulty = "" #сложность игры, понадобится в статистике

    if max_value <= 50: 
        attempts = 10
        difficulty = "Легкая"

    elif 50 < max_value <= 100:
        attempts = 7
        difficulty = "Средняя"

    elif 100 < max_value <= 1000:
        attempts = 10
        difficulty = "Сложная" #верхняя граница определяет уровень сложности

    start_number_attempts = attempts #количество попыток, которое было вначале(тоже для статистики)
    imaginary_number = random.randint(1, max_value) #число компьютера
    
    while True:

        attempts -= 1
        answer = response_check(max_value=max_value, prompt=f"Твоя догадка? ", user_response=0) #наше предположение

        if imaginary_number > answer:
            print("Моё число больше твоего")

        elif imaginary_number < answer:
            print("Моё число меньше твоего")

        else:
            print(f"Ты угадал! Моё число было {imaginary_number}")
            endgame_state = "Выиграна"
            break

        if attempts == 0:
            print("Кажется у тебя закончились попытки, ты проиграл!")
            endgame_state = "Проиграна"
            break

        print(f"Оставшиеся попытки: {attempts}")

    savestats(attempts,start_number_attempts, difficulty, endgame_state)
    play_again() 


def play_again(): #рестарт игры

    choice = input("Хочешь сыграть ещё раз? (да/нет): ")

    if choice == "да":
        print("Выбирай тогда сложность")
        main()

    else:
        print("Мммм, ну ладно")

def response_check(prompt, user_response, max_value): #валидация ввода игроком числа. Оно не может быть меньше 1 и больше верхней границы
    
    while True:
        try:

            user_response = int(input(prompt))

            if 1 <= user_response <= max_value:
                return user_response
            print(f"Я чувствую что твое число выходит за рамки от 1 до {max_value}")

        except ValueError:
            print("это даже не число...")

def difficulty_choose(): #игрок здесь выбирает сложность. Тут тоже смотрим чтобы он ввел правильное значение
    
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
            print("Введи число от 1 до 3!")    

        except ValueError:
            print("это даже не число...")

GREETINGS = """Привет! Давай поиграем? Я загадываю число, а
ты пытаешься его угадать за определенное число попыток. Если тебе
не удастся отгадать число, то ты проиграешь, если получится, ты победишь и я тебя похвалю(нет).
Согласен? Для начала выбери уровень сложности, просто поставь цифру ниже:
"""
GREETINGS_EASY_DIFFICULTY_CHOOSE = "1 - Легкий: от 1 до 50. 10 попыток"
GREETINGS_MEDIUM_DIFFICULTY_CHOOSE = "2 - Средний: от 1 до 100. 7 попыток"
GREETINGS_HARD_DIFFICULTY_CHOOSE = "3 - Сложный: от 1 до 1000. 10 попыток"

print(GREETINGS)
print(GREETINGS_EASY_DIFFICULTY_CHOOSE)
print(GREETINGS_MEDIUM_DIFFICULTY_CHOOSE)
print(GREETINGS_HARD_DIFFICULTY_CHOOSE)

def savestats(attempts_results, start_attempts_results, difficulty_results, endgame_condition): 
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    GAME_OVER_STATS = f"""Игра была: {endgame_condition} | {timestamp} 
    | Осталось попыток: {attempts_results}
        из {start_attempts_results} возможных | Сложность игры: {difficulty_results}"""
    
    with open("stats2.txt", "a", encoding="utf-8") as f:
        f.write(GAME_OVER_STATS)
        
main()
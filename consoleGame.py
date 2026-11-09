import random
import json
import difflib
choices = ["камень", "ножницы", "бумага"]
valid_choices = choices + ["выход"]
class ScoreBoard:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
    def update_score(self, result):
        if "Вы выиграли" in result:
            self.user_score += 1
        elif "Вы проиграли" in result:
            self.computer_score += 1
    def display_score(self):
        print(f"Счет: Вы {self.user_score} - Компьютер {self.computer_score}")
    def save_score(self):
        score_data = {
            "user_score": self.user_score,
            "computer_score": self.computer_score
        }
        with open("score_console.json", "w", encoding="utf-8") as file:
            json.dump(score_data, file)
def correct_input(user_input):
    user_input = user_input.lower().strip()
    if user_input in valid_choices:
        return user_input
    choices_in_input = [choice for choice in choices if choice in user_input]
    if len(choices_in_input) > 1:
        return None
    closest_match = difflib.get_close_matches(user_input, valid_choices, n=1, cutoff=0.6)
    if closest_match:
        return closest_match[0]
    return None
def win_or_lose(user_choice, computer_choice):
    if user_choice == computer_choice:
        return f"Ничья! Вы оба выбрали {user_choice}."
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
        (user_choice == "ножницы" and computer_choice == "бумага") or \
        (user_choice == "бумага" and computer_choice == "камень"): 
        return "Вы выиграли! Компьютер выбрал " + computer_choice + "."
    elif (user_choice == "камень" and computer_choice == "бумага") or \
        (user_choice == "ножницы" and computer_choice == "камень") or \
        (user_choice == "бумага" and computer_choice == "ножницы"):
        return "Вы проиграли! Компьютер выбрал " + computer_choice + "."
scoreboard = ScoreBoard()
while True:
        user_choice = correct_input(input("Выберите камень, ножницы или бумагу: "))
        if user_choice == "выход":
            scoreboard.save_score()
            print("Игра завершена.")
            break
        if user_choice is None:
            print("Неверный выбор. Пожалуйста, выберите камень, ножницы или бумагу.")
            continue
        computer_choice = random.choice(choices)
        result = win_or_lose(user_choice, computer_choice)
        scoreboard.update_score(result)
        print(result)
        scoreboard.display_score()
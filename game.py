import random
choices = ["камень", "ножницы", "бумага"]
exit_command = "выход"
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
while True:
        user_choice = input("Выберите камень, ножницы или бумагу: ")
        if user_choice == exit_command:
            print("Игра завершена.")
            break
        if user_choice not in choices:
            print("Неверный выбор. Пожалуйста, выберите камень, ножницы или бумагу.")
            continue
        computer_choice = random.choice(choices)
        result = win_or_lose(user_choice, computer_choice)
        print(result)
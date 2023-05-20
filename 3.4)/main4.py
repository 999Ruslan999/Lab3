import random

count_correct = 0
count_wrong = 0

while count_wrong < 3:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 + num2
    user_answer = input(f"{num1} + {num2} = ")
    if int(user_answer) == answer:
        print("Правильно!")
        count_correct += 1
    else:
        print("Ответ неверный")
        count_wrong += 1

print(f"Игра окончена. Правильных ответов: {count_correct}")
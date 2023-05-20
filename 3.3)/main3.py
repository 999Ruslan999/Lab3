words = []

while True:
    word = input("Введите слово: ")
    if word == "stop":
        break
    words.append(word)

for word in words:
    if "ф" in word.lower():
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")

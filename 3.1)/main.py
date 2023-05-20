n = int(input("Введите количество слов: "))
words = []

for i in range(n):
    word = input("Введите слово: ")
    words.append(word)

result = " ".join(words)
print(result)

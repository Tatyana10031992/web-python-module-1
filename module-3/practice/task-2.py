text = input("Введите текст: ")
words = input("Введите слово: ").split()

for word in words:
    text = text.replace(word, word.upper())

print(text)  

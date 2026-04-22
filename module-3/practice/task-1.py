text = input("Введите предложение: ")
new_text = "".join(i for i in text if i.isalnum()).lower()
if new_text == new_text[::-1]:
    print(text, "Это палиндром")
else:
    print(text, "Это не палиндром")

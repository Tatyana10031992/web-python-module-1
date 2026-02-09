dictionary = {}

def getinput(prompt): 
    return input(prompt).strip().lower()

def add_word():
    eng = getinput("Введите английское слово: ")
    fr = getinput("Введите французский перевод: ")  
    
    if eng in dictionary:
        print("Слово уже есть. Используйте 'заменить' для обновления.")
    else:
        dictionary[eng] = fr
        print(f"Слово '{eng}' добавлено (перевод: '{fr}').")

def delete_word():
    eng = getinput("Введите английское слово для удаления: ")
    
    if eng in dictionary:
        del dictionary[eng]
        print(f"Слово '{eng}' удалено.")
    else:
        print("Слово не найдено.")

def search_word():
    eng = getinput("Введите английское слово для поиска: ")
    
    if eng in dictionary:
        print(f"{eng} — {dictionary[eng]}")
    else:
        print("Слово не найдено.")

def update_word():
    eng = getinput("Введите английское слово для замены: ")
    
    if eng in dictionary:
        fr = getinput("Введите новый французский перевод: ")  
        dictionary[eng] = fr
        print(f"Перевод для '{eng}' обновлён.")  
    else:
        print("Слово не найдено. Используйте 'добавить' для нового слова.")

def show_all():
    if not dictionary:
        print("Словарь пуст.")
        return
    print("\nВСЕ СЛОВА:")
    for eng, fr in sorted(dictionary.items()):
        print(f"{eng} — {fr}")
    print("=" * 30)

def main():
    commands = {
        "добавить": add_word,
        "удалить": delete_word,
        "поиск": search_word,
        "заменить": update_word,
        "показать": show_all,
        "выход": lambda: print("До свидания!") or exit()
    }
    print("Команды: добавить, удалить, поиск, заменить, показать, выход")
    
    while True:
        cmd = getinput("\nВведите команду: ")
        action = commands.get(cmd)
        if action:
            action()
            if cmd == "выход":
                break
        else:
            print("Неизвестная команда. Попробуйте: добавить, удалить, поиск, заменить, показать, выход")

if __name__ == "__main__":
    main()

        
     
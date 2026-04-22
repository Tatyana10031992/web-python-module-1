library = {}

def get_input(prompt):
    value = input(prompt).strip()
    if not value:
        print("Значение не может быть пустым.")
        return None
    return value

def add_book():
    title = get_input("Введите название книги: ")
    if not title:
        return
    if title in library:
        print("Книга уже есть.")
        return

    library[title] = {
        "Автор": get_input("Автор: "),
        "Жанр": get_input("Жанр: "),
        "Год выпуска": get_input("Год выпуска: "),
        "Страниц": get_input("Количество страниц: "),
        "Издательство": get_input("Издательство: ")
    }

    
    if all(library[title].values()):
        print(f"Книга '{title}' добавлена.")
    else:
        print("Не все поля заполнены. Книга не добавлена.")
        del library[title]

def remove_book():
    title = get_input("Введите название книги для удаления: ")
    if not title or title not in library:
        print("Книга не найдена.")
        return
    del library[title]
    print(f"Книга '{title}' удалена.")

def search_book():
    title = get_input("Введите название книги для поиска: ")
    if not title or title not in library:
        print("Книга не найдена.")
        return

    print(f"\nДанные о книге '{title}':")
    for key, value in library[title].items():
        print(f"{key}: {value}")

def update_book():
    title = get_input("Введите название книги для обновления: ")
    if not title or title not in library:
        print("Книга не найдена.")
        return

    fields = list(library[title].keys())
    print("Выберите поле для обновления:")
    for idx, field in enumerate(fields, 1):
        print(f"{idx}. {field}")

    try:
        choice = int(input("Введите номер поля: "))
        if 1 <= choice <= len(fields):
            new_value = get_input(f"Новый {fields[choice-1]}: ")
            if new_value:
                library[title][fields[choice-1]] = new_value
                print(f"{fields[choice-1]} обновлено.")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Введите число.")

def show_all():
    if not library:
        print("Коллекция пуста.")
        return

    print("\nВСЕ КНИГИ В КОЛЛЕКЦИИ:")
    for title, info in library.items():
        print(f"\nНазвание: {title}")
        for key, value in info.items():
            print(f"{key}: {value}")
    print("=" * 40)

def main():
    commands = {
        "добавить": add_book,
        "удалить": remove_book,
        "поиск": search_book,
        "заменить": update_book,
        "показать": show_all,
        "выход": lambda: print("До свидания!")
    }
    print("Команды: добавить, удалить, поиск, заменить, показать, выход")

    while True:
        cmd = input("\nВведите команду: ").strip().lower()
        action = commands.get(cmd)

        if action:
            action()
            if cmd == "выход":
                break
        else:
            print("Неизвестная команда. Попробуйте ещё раз.")

if __name__ == "__main__":
    main()

    
person_data = {}

def get_fio(prompt):  
    fio = input(prompt).strip()
    if not fio:
        print("ФИО не может быть пустым.")
        return None
    return fio

def person_exists(fio):
    if fio not in person_data:
        print("Этот человек не найден.")
        return False
    return True

def add_person():
    fio = get_fio("Введите ФИО: ")  
    if not fio:
        return

    if fio in person_data:
        print("Этот человек уже есть.")
        return

    person_data[fio] = {
        "Телефон": input("Телефон: ").strip(),       
        "Email": input("Рабочий Email: ").strip(),   
        "Должность": input("Должность: ").strip(),    
        "Кабинет": input("Номер кабинета: ").strip(),   
        "Skype": input("Skype: ").strip()            
    }
    print(f"Данные для {fio} добавлены.")

def remove_person():
    fio = get_fio("Введите ФИО для удаления: ")  
    if not fio or not person_exists(fio):
        return

    del person_data[fio]
    print(f"{fio} удалён из базы.")  

def search_person():
    fio = get_fio("Введите ФИО для поиска: ") 
    if not fio or not person_exists(fio):
        return

    print(f"Данные для {fio}:")
    for key, value in person_data[fio].items():
        print(f"{key}: {value}")

def update_person():
    fio = get_fio("Введите ФИО для обновления: ") 
    if not fio or not person_exists(fio):
        return

    fields = list(person_data[fio].keys())
    print("Выберите поле для обновления:")
    for idx, field in enumerate(fields, 1):
        print(f"{idx}. {field}")

    try:
        choice = int(input("Введите номер поля: ").strip())  
        if 1 <= choice <= len(fields):
            new_value = input(f"Введите новый {fields[choice-1]}: ").strip()
            person_data[fio][fields[choice-1]] = new_value
            print(f"{fields[choice-1]} обновлено.")
        else:
            print("Неверный выбор.")
    except ValueError:
        print("Введите число.")

def show_all():
    if not person_data:
        print("База пуста.")
        return

    for fio, info in person_data.items():
        print(f"\nФИО: {fio}")
        for key, value in info.items():
            print(f"{key}: {value}")
    print("=" * 30)

def main():
    commands = {
        "добавить": add_person,
        "удалить": remove_person,
        "поиск": search_person,
        "заменить": update_person,
        "показать": show_all,
        "выход": lambda: print("До свидания!") or exit()
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
            print("Неизвестная команда.")

if __name__ == "__main__":
    main()

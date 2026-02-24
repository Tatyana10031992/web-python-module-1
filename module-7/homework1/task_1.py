def load_employees(filename):
    employees = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 4:
                    continue
                surname, name, age_str, position = parts
                if not age_str.isdigit():
                    continue
                employees.append({
                    "Фамилия": surname,
            "Имя": name,
            "Возраст": int(age_str),
            "Должность": position
        })
    except FileNotFoundError:
        print("Файл не найден, создан пустой список.")
    return employees


def save_employees(filename, employees):
    with open(filename, "w", encoding="utf-8") as f:
        for e in employees:
            f.write(f"{e['Фамилия']},{e['Имя']},{e['Возраст']},{e['Должность']}\n")
    print(f"Данные сохранены в '{filename}'.")

def input_employee():
    surname = input("Фамилия: ").strip()
    name = input("Имя: ").strip()
    while True:
        age_str = input("Возраст: ").strip()
        if age_str.isdigit():
            age = int(age_str)
            break
        else:
            print("Возраст должен быть числом")
    position = input("Должность: ").strip()
    return {"Фамилия": surname, "Имя": name, "Возраст": age, "Должность": position}

def find_by_surname(employees, surname):
    return [e for e in employees if e["Фамилия"].lower() == surname.lower()]

def find_by_age(employees, age):
    return [e for e in employees if e["Возраст"] == age]

def find_by_surname_start(employees, letter):
    letter = letter.lower()
    return [e for e in employees if e["Фамилия"].lower().startswith(letter)]

def print_employees(employees):
    if not employees:
        print("Сотрудники не найдены")
        return
    for i, e in enumerate(employees, 1):
        print(f"{i}. {e['Фамилия']} {e['Имя']}, {e['Возраст']} лет, Должность: {e['Должность']}")

def edit_employee(employee):
    print("Введите новые данные (оставьте пустым, чтобы не менять):")
    surname = input(f"Фамилия [{employee['Фамилия']}]: ").strip()
    if surname:
        employee['Фамилия'] = surname
    name = input(f"Имя [{employee['Имя']}]: ").strip()  
    if name:
        employee['Имя'] = name
    age_str = input(f"Возраст [{employee['Возраст']}]: ").strip()
    if age_str:
        if age_str.isdigit():
            employee['Возраст'] = int(age_str)
        else:
            print("Возраст введён некорректно, значение не изменено.")
    position = input(f"Должность [{employee['Должность']}]: ").strip()
    if position:
        employee['Должность'] = position
    print("Данные обновлены.")

def save_found_to_file(employees):
    if not employees:
        print("Нечего сохранять.")
        return
    filename = input("Введите имя файла для сохранения сотрудников: ").strip()
    if not filename:
        print("Имя файла не может быть пустым.")
        return
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for e in employees:
                f.write(f"{e['Фамилия']},{e['Имя']},{e['Возраст']},{e['Должность']}\n")
        print(f"Найденные сотрудники сохранены в файл '{filename}'.")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")

def main():
    filename = input("Введите имя файла для загрузки: ").strip()
    employees = load_employees(filename)

    while True:
        print("1. Добавить сотрудника")
        print("2. Редактировать сотрудника по фамилии")
        print("3. Удалить сотрудника по фамилии")
        print("4. Поиск сотрудника по фамилии")
        print("5. Вывести всех сотрудников")
        print("6. Сохранить список сотрудников в файл")
        print("7. Выход")

        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            emp = input_employee()
            employees.append(emp)
            print("Сотрудник добавлен.")
        elif choice == "2":
            surname = input("Введите фамилию сотрудника для редактирования: ").strip()
            found = find_by_surname(employees, surname)
            if not found:
                print("Сотрудник с такой фамилией не найден.")
            elif len(found) == 1:
                edit_employee(found[0])
            else:
                print("Найдено несколько сотрудников с такой фамилией:")
                print_employees(found)
                idx_str = input("Введите номер сотрудника для редактирования: ").strip()
                if idx_str.isdigit():
                    idx = int(idx_str)
                    if 1 <= idx <= len(found):
                        edit_employee(found[idx-1])
                    else:
                        print("Неверный номер.")
                else:
                    print("Неверный ввод.")
        elif choice == "3":
            surname = input("Введите фамилию сотрудника для удаления: ").strip()
            found = find_by_surname(employees, surname)
            if not found:
                print("Сотрудник с такой фамилией не найден.")
            elif len(found) == 1:
                employees.remove(found[0])
                print("Сотрудник удалён.")
            else:
                print("Найдено несколько сотрудников с такой фамилией:")
                print_employees(found)
                idx_str = input("Введите номер сотрудника для удаления: ").strip()
                if idx_str.isdigit():
                    idx = int(idx_str)
                    if 1 <= idx <= len(found):
                        employees.remove(found[idx-1])
                        print("Сотрудник удалён.")
                    else:
                        print("Неверный номер.")
                else:
                    print("Неверный ввод.")
        elif choice == "4":
            surname = input("Введите фамилию сотрудника для поиска: ").strip()
            found = find_by_surname(employees, surname)
            print_employees(found)
            if found:
                save_opt = input("Сохранить найденных сотрудников в файл? (д/н): ").strip().lower()
                if save_opt == "д":
                    save_found_to_file(found)
        elif choice == '5':
            print_employees(employees)
        elif choice == '6':
            save_employees(filename, employees)
        elif choice == '7':
            save_employees(filename, employees)
            print("Выход из программы.")
            break
        else:
            print("Неверный пункт меню. Повторите ввод.")

if __name__ == "__main__":
    main()

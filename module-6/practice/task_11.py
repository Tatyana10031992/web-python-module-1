def get_valid(prompt):
    while True:
        try:
            grade = int(input(prompt))
            if 1 <= grade <= 12:
                return grade
            print("Ошибка: оценка должна быть от 1 до 12. Попробуйте снова.")
        except ValueError:
            print("Ошибка: введите целое число. Попробуйте снова.")


def get_valid_index(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Ошибка: значение должно быть от {min_val} до {max_val}.")
        except ValueError:
            print("Ошибка: введите целое число.")

def main():
    print("Введите 10 оценок от 1 до 12:")
    grades = [get_valid(f"Оценка {i+1}: ") for i in range(10)]

    while True:
        print("\nМеню:")
        print("1. Вывести оценки")
        print("2. Пересдача экзамена")
        print("3. Выходит ли стипендия")
        print("4. Вывести отсортированный список оценок")
        print("5. Выход")

        choice = input("Выберите пункт (1–5): ").strip()

        if choice == "1":
            print("Оценки:", grades)

        elif choice == "2":
            index = get_valid_index("Введите номер оценки (1–10): ", 1, 10)
            new_grade = get_valid("Введите новую оценку (1–12): ")
            grades[index - 1] = new_grade
            print("Оценка обновлена.")

        elif choice == "3":
            average = sum(grades) / len(grades)
            status = "выходит" if average >= 10.7 else "не выходит"
            print(f"Средний балл {average:.2f}. Стипендия {status}.")

        elif choice == "4":
            order = input("Введите 'возрастанию' или 'убыванию': ").strip().lower()
            if order in ('возрастанию', 'возрастание'):
                sorted_grades = sorted(grades)
            elif order == "убыванию":
                sorted_grades = sorted(grades, reverse=True)
            else:
                print("Некорректный ввод. Попробуйте снова.")
                continue
            print("Отсортированный список оценок:", sorted_grades)

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()

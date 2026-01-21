elements = list(map(int, input("Введите элементы списка через пробел: ").split()))
target_number = int(input("Введите число для поиска: "))
count = 0
for number in elements:
    if number == target_number:
        count += 1



print(f"Число {target_number} встречается в списке {count}")

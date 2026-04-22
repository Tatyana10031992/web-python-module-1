str = input("Введите целые числа от 0 до 50:")

numbers = list(map(int, str.split()))

sum_negative = sum(num for num in numbers if num < 0)
print(f"Сумма отрицательных чисел: {sum_negative}")

sum_even = sum(num for num in numbers if num % 2 == 0)
print(f"Сумма четных чисел: {sum_even}")

sum_odd = sum(num for num in numbers if num % 2 != 0)
print(f"Сумма нечетных чисел: {sum_odd}")

product_indices_3 = 1
has_product_indeces_3 = False
for i in range(0, len(numbers), 3):
    product_indices_3 *= numbers[i]
    has_product_indeces_3 = True
if not has_product_indeces_3:
    product_indices_3 = 0
print(f"Произведение элементов с индексами кратными 3: {product_indices_3}")

min_val = min(numbers)
max_val = max(numbers)
min_index = numbers.index(min_val)
max_index = numbers.index(max_val)

start = min(min_index, max_index) + 1
end = max(min_index, max_index)

product_between_min_max = 1
has_product_between = False
for i in range(start, end):
    product_between_min_max *= numbers[i]
    has_product_between = True
if not has_product_between:
    product_between_min_max = 0
print(f"Произведение элементов между min и max: {product_between_min_max}")






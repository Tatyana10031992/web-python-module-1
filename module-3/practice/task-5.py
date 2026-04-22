import random
n = 10  
min_val, max_val = -30, 30 
numbers = [random.randint(min_val, max_val) for _ in range(n)]

print("Сгенерированный список:", numbers)


min_element = min(numbers)
max_element = max(numbers)

negative_count = sum(1 for x in numbers if x < 0)
positive_count = sum(1 for x in numbers if x > 0)
zero_count = sum(1 for x in numbers if x == 0)


print(f"Минимальный элемент: {min_element}")
print(f"Максимальный элемент: {max_element}")
print(f"Количество отрицательных: {negative_count}")
print(f"Количество положительных: {positive_count}")
print(f"Количество нулей: {zero_count}")

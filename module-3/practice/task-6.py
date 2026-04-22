import random

n = 10
min_val = -30
max_val = 30

list1 = [random.randint(min_val, max_val)for _ in range(n)]
list2 = [random.randint(min_val, max_val)for _ in range(n)]

print("Список 1:",list1)
print("Список 2:",list2)

combined = list1 + list2
print("Объединенный список:", combined)

unique_all = list(set(combined))
print("Без повторений:", unique_all)

common = list(set(list1) & set(list2))
print("Общие элементы:", common)

unique_each = list(set(list1) ^ set(list2))
print("Уникальные для каждого:", unique_each)

min_max_list1 = [min(list1), max(list1)]
min_max_list2 = [min(list2), max(list2)]
min_max_combined = min_max_list1 + min_max_list2
print("Мин/макс каждого:", min_max_combined)

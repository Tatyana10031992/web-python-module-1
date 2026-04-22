d = {}

n = int(input("Сколько пар ключ значение хотите добавить?"))

for i in range(n):
    key = input(f"Введите ключ {i+1}:")
    value = input(f"Введите значение для ключа:")
    d[key] = value

print("Созданный словарь:")
for key, value in d.items():
    print(f"{key}={value}")
    

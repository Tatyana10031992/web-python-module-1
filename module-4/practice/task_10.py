def sum_range(a,b):
    if a == b:
        return a 

    else:
        return a + sum_range(a + 1, b)

a = int(input("Введите начало диапазона(a):"))
b = int(input("Введите конец диапазона(b):"))

result =  sum_range(a,b)
print(f"Сумма чисел от {a} до {b} равно {result}")
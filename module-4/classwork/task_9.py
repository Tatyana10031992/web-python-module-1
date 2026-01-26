def power(x,n):
    # Базовый случай
    if n == 1:
        return x

     # Рекурсивный шаг
    return x * power(x, n - 1)
print(power(2, 3))

def func(num):
    numbers = [int(d) for d in str(num)]
    a = sum(numbers[:3])
    b = sum(numbers[3:])
    if a == b:
        print("Счастливое")
    else:
        print("Несчастливое")
func(723422)
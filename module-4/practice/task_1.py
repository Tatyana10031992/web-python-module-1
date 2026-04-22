# def func_9(obj):
#     print(obj)

# func_9({"a": 1, "b": 2})







# def func_8(num1, num2, *args, **kwargs):
#     print(f"{num1}, {num2}")
#     print(args)
#     print(kwargs)

# func_8(1, 2, 3, 4, 5, name=1)






# def func_7(**kwargs):
#     print(kwargs)

# func_7(name=1, age=2)







# def func_6(*args):
#     total = 0
#     for num in args:
#         total += num
    
#     print(total)

# func_6(1,2,3,4,5)





# def func_4(name, age, city):
#     print(f"{name}-{age}-{city}")

# func_4("Татьяна", "33", "Чебоксары")



# def func_1():
#     print("Функция")
# func_1()

# def func_2():
#     return "Привет func_2"

# def func_3():
#     pass

# func_1()
# print(func_2())


# Задание 2

def func(num1, num2):

    for num in range(num1, num2):
        if num % 2 !=0:
            print(num)
func(5,10)

# Задание 3

def func(length, direction, symbol):
    if direction == "horizontal":
        print(symbol * length)
    if direction == "vertical":
        for length in range(length):
            print(symbol)

func(5, "horizontal", "#" )
func(10, "vertical", "!")

        



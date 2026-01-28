my_set = {1,2,3}
print(3 in my_set)
print(5 not in my_set)
print(len(my_set))     #Длина множества
print(sum(my_set))     #Сумма множеств
print(min(my_set), max(my_set))  # Мин\Макс число в множество

for num in my_set:
    print(num)


#Операция над множествами
#4.Симметрическая разность
set_a = {1,2,3,4}
set_b = {3,4,5,6}
result = set_a.symmetric_difference(set_b)   #Метод
result_operator = set_a ^ set_b               #Оператор
set_a ^= set_b                                #Присваивание
print(set_a,result,result_operator)



#3.Разность
set_a = {1,2,3,4,5}
set_b = {4,5,6,7.8}
result = set_a.difference(set_b)   #Метод
result_operator = set_a - set_b    #Оператор
set_a -= set_b                     #Присваивание
print(set_a,result,result_operator)



#2.Пересечение
set_a = {1,2,3,4}
set_b = {3,4,5,6}
result = set_a.intersection(set_b) #Метод
result_operator = set_a & set_b  #Оператор
set_a &= set_b                    #Присваивание
print(set_a, result,result_operator)

#1.Объединение
set_a = {1,2,3,4}
set_b = {4,5,6,7}
result = set_a.union(set_b)  #Метод
result_operator = set_a | set_b #Оператор
set_a |= set_b #Присвоение
print(set_a, result, result_operator)


#Удаление элементов
# fruits = {"яблоко", "банан", "апельсин"}
# fruits.remove("яблоко")
# fruits.discard("груша")
# fruits.pop()
# print(fruits)


#Добавление элементов
# fruits = {"яблоко", "банан", "апельсин"}
# fruits.add("груша")
# fruits.update(["смородина", "клубника"])
# print(fruits)


#Генератор множеств
# my_set = {x for x in range(5)}
# print(my_set)


#--------------
# set_tuple = set((1,1,2,2,3))
# print(set_tuple)

# #------------
# letters = set("привет")
# print(letters)

# #------------
# my_set_1 = set({1,2,2,3,3,4})
# print(my_set_1)

# #------------
# my_set = {1,1,2,2,3,3}
# print(my_set)
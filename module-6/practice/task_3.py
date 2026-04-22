fruits = ["banana", "apple", "bananamango", "mango", "strawberry-banana"]
fruits_count = input("Введите название фрукта:")

counts = 0
for item in fruits:
    if fruits_count in item:
        counts += 1
print(counts)


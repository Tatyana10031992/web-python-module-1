cars = ["мерседес","бмв", "лада","ауди"]
manufacturer = input("Введите название производителя:")
replacement = input("Введите название для замены:")


new_br = []
for car in cars:
    if car == manufacturer:
        new_br.append(replacement)
    else:
        new_br.append(car)

print(new_br)


    

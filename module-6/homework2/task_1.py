def main():
    codes = [102,56]
    phones = [89519976438, 89276693933]
    
    while True:
        print("\nМеню:")
        print("1.Отсортировать по идентификационным кодам")
        print("2.Отсортировать по номерам телефонов")
        print("3.Вывести список пользователей")
        print("4.Выход")
        
        choice = input("Выберите пунк меню(1-4)").strip()
        
        if choice == "1":
            codes, phones = zip(*sorted(zip(codes,phones), key=lambda x: x[0]))
            codes, phones = list(codes), list(phones)
            print("Сортировка по кодам выполнена.")
            
        elif choice == "2":
            codes, phones = zip(*sorted(zip(codes,phones), key=lambda x: x[1]))
            codes, phones = list(codes), list(phones)
            print("Сортировка по номерам выполнена.")
            
            
        elif choice == "3":
            print("\nСписок пользователей:")
            for c,p in zip(codes, phones):
                print(f"Код: {c}, Телефон: {p}")
                
        elif choice == "4":
            print("Выход из программы.")
            break
        
        else:
              print("Некоректный выбор.Попробуйте снова.")
              
if __name__=="__main__":
    main()
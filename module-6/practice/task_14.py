def main():
    books = ["Война и мир", "Мастер и маргарита", "Преступление и наказание", "Отцы и дети"]
    years = [1869, 1976, 1866, 1862]
    
    while True:
        print("\nМеню:")
        print("1. Отсортировать по названию книг")
        print("2. Отсортировать по годам выпуска")
        print("3. Вывести список книг")
        print("4. Выход")
        
        choice = input("Выберите пункт меню (1-4)").strip()
        
        if choice == "1":
            books, years = map(list, zip(*sorted(zip(books, years), key=lambda x: x[0])))
            print("Сортировка по названиям выполнена.")
            
        elif choice == "2":
            books, years = map(list, zip(*sorted(zip(books, years), key=lambda x: x[1])))
            print("Сортировка по годам выполнена.")
                
                
        elif choice == "3":
            print("\nСписок книг:")
            for book, year in zip(books, years):
                print(f"Название: {book}, Год: {year}")
                 
        elif choice == "4":
             print("Выход из программы.")
             break
         
        else:
             print("Некорректный выбор. Попробуйте снова.")
             
if __name__=="__main__":
    main()
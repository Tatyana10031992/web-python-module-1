basketball_players = {}

def add_player():
    name = input("ФИО: ").strip()
    if not name:
        print("ФИО не может быть путым.")
        return
    try:
        height = int(input("Рост(см): "))
        if height <= 0:
            raise ValueError
    except:
        print("Некорректный рост.")
        return
    if name in basketball_players:
        print("Этот игрок уже есть в базе.")
    else:
        basketball_players[name] = height
        print(f"{name} добавлен, рост: {height} см.")

def remove_player():
    name = input("ФИО для удаления: ").strip()
    if not name:
        print("ФИО не может быть путым.")
        return
    if name in basketball_players:
        del basketball_players[name]
        print(f"{name} удален.")
    else:
        print("Игрок не найден.")

def find_player():
    name = input("ФИО для поиска: ").strip()
    if not name:
        print("ФИО не может быть путым.")
        return
    if name in basketball_players:
        print(f"{name}, рост: {basketball_players[name]} см")
    else:
        print("Игрок не найден.")

def show_all_players():
    if not basketball_players:
        print("Пусто.")
        return
    print("\nВСЕ БАСКЕТБОЛИСТЫ:")
    for name, height in sorted(basketball_players.items()):
        print(f"{name} - {height} см")
    print("=" * 20)

def main():
    commands = {
        "добавить": add_player,
        "удалить": remove_player,
        "поиск": find_player,
        "показать": show_all_players
    }
    print("Команды: добавить, удалить, поиск, показать, выход")
    while True:
        cmd = input("\nВведите команду: ").strip().lower()
        if cmd == "выход":
            print("До свидания!")
            break
        elif cmd in commands:
            commands[cmd]()
        else:
            print("Неверная команда.")

if __name__ == "__main__":
    main()
import random

def generate_number():
    
    digits = list(range(10))
    random.shuffle(digits)
    if digits[0] == 0:
        digits[0], digits[1] = digits[1], digits[0]
    return ''.join(map(str, digits[:4])) 

def count_bulls_and_cows(secret, guess):
   
    cows = 0
    secret_remaining = []
    guess_remaining = []

    for i in range(4):
        if guess[i] == secret[i]:
            cows += 1
        else:
            secret_remaining.append(secret[i])
            guess_remaining.append(guess[i])

    
    bulls = len(set(guess_remaining) & set(secret_remaining))
    return cows, bulls

def game_recursive(secret, attempts=0):
    if attempts >= 10:
        print(f"Попытки исчерпаны! Число было {secret}.")
        return
    guess = input("Введите 4‑значное число: ").strip()

  
    if not (guess.isdigit() and len(guess) == 4 and len(set(guess)) == 4):
        print("Ошибка: введите 4 разные цифры (например, 1234).")
        game_recursive(secret, attempts)
        return

    attempts += 1
    cows, bulls = count_bulls_and_cows(secret, guess)
    print(f"Коровы: {cows}, Быки: {bulls}")

    if cows == 4:
        print(f"Победа! Вы угадали число {secret} за {attempts} попыток.")
    else:
        game_recursive(secret, attempts)
        
    

def main():
    print("Добро пожаловать в игру «Быки и коровы»!")
    print("Я загадал 4‑значное число с неповторяющимися цифрами.")
    print("Попробуйте угадать его!")
    secret = generate_number()
    game_recursive(secret)

if __name__ == "__main__":
    main()

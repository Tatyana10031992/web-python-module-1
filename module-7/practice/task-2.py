def analyze_text_file(input_path, output_path):
    vowels = "ауоыиэеёюяАУОЫИЭЕЁЮЯaeiouAEIOU"
    consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    digits = "0123456789"

    num_chars = 0
    num_lines = 0
    num_vowels = 0
    num_consonants = 0
    num_digits = 0

    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            num_chars += len(line.rstrip('\n\r'))  
            num_lines += 1
            num_vowels += sum(ch in vowels for ch in line)
            num_consonants += sum(ch in consonants for ch in line)  
            num_digits += sum(ch in digits for ch in line)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(
            f"Количество символов: {num_chars}\n"
            f"Количество строк: {num_lines}\n"
            f"Количество гласных букв: {num_vowels}\n"
            f"Количество согласных букв: {num_consonants}\n"
            f"Количество цифр: {num_digits}\n"
        )


analyze_text_file("input.txt", "statistics.txt")

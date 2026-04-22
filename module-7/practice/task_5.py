def count_word_occurrences(file_path, target_word):
    target_word = target_word.lower() 
    count = 0
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            count += line.lower().split().count(target_word)
    return count

file_path = "input3.txt"
word = input("Введите слово для поиска:")
print(count_word_occurrences(file_path,word))
def replace_word_in_file(input_path, output_path, old_word, new_word):
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()
    
   
    replaced_text = text.replace(old_word, new_word)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(replaced_text)

input_file = "input4.txt"
output_file = "output1.txt"
old = input("Введите слово для поиска: ")
new = input("Введите слово для замены: ")

replace_word_in_file(input_file, output_file, old, new)
print(f"Слово '{old}' заменено на '{new}' в файле '{output_file}'.")

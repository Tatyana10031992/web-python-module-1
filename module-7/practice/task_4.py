def find_longest_line_length(file_path):
    max_length = 0
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            current_length = len(line.rstrip("\n\r"))
            max_length = max(max_length, current_length)
    return max_length

file_path = "input2.txt"
length = find_longest_line_length(file_path)
print(length)
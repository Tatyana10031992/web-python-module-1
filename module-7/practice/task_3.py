def remove_last_line(input1_path, output_path):
    with open(input1_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    if lines:
        lines = lines[:-1]
        
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

remove_last_line("input1.txt", "output.txt")
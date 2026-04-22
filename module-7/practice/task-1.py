def compare_files(file1_path, file2_path):
    with open(file1_path, "r", encoding="utf-8") as f1, \
         open(file2_path, "r", encoding="utf-8") as f2:

        line_num = 1
        mismatch_found = False
        while True:
            line1 = f1.readline()
            line2 = f2.readline()

            if not line1 and not line2:
                break

            l1 = line1.rstrip("\n\r")
            l2 = line2.rstrip("\n\r")

            if l1 != l2:
                print(f"Несовпадение на строке {line_num}:")
                print(f"Файл1: {l1}")
                print(f"Файл2: {l2}")
                mismatch_found = True

            line_num += 1

        if not mismatch_found:
            print("Файлы совпадают.")



compare_files("file1.txt", "file2.txt")
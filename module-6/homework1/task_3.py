my_list = [64, 34, 25, 12, 12, 11, 90]

def bubble_sort_improved(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

print("До сортировки:", my_list)
print("После сортировки:",bubble_sort_improved(my_list) )
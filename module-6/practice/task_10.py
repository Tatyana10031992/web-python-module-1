lst = [5, 8, 1, 7, 3, 9]

def process_list(lst):
    if not lst:
        return lst

    n = len(lst)
    mean_value = sum(lst) / n

    two_thirds = 2 * n // 3
    one_third = n // 3

    result = lst.copy()

    if mean_value > 0:
        result[:two_thirds] = sorted(result[:two_thirds]) 
    else:
        result[:one_third] = sorted(result[:one_third]) 

    result[two_thirds:] = result[two_thirds:][::-1]

    return result


print("Исходный список:", lst)
processed_lst = process_list(lst)
print("Обработанный список:", processed_lst)

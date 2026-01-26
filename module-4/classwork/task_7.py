def flat(nasted_list):
    flat_arr = []
    for item in nasted_list:
        for item_child in item:
            flat_arr.append(item_child)
    return flat_arr
    
    


print(flat([[1,2,3],[4,5],[6]]))
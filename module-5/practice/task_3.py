def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr [j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# [ 8, 3, 7, 1]
# n = 4
# gap = 2

# i = 2
# temp = 7
# j = 2

# arr[j - gap] = arr[0] = 8
# j = 0
# [ 7, 3, 8, 1]
# ------------
# i = 3
# temp = 1
# j = 3
# arr[j - gap] = arr[3 - 2] = arr[1] = 3
# [7, 1, 8, 3]
# gap = 1
# [1, 7, 3, 8]
# [1, 3, 7, 8]
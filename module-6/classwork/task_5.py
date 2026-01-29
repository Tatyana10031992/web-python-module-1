numbers = [1,25,345,6789,12,89,123]
result = {}

for num in numbers:
    digit_length = len(str(abs(num)))
    result [digit_length] = result.setdefault(digit_length,0) + 1

for item in sorted(result):
    print(item, result[item])





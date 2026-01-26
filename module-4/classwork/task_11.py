def print_stars(n):
    if n == 0:
        return ""
    return "*" + print_stars(n - 1)

print(print_stars(1))

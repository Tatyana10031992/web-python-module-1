math=input('Введите арифметическое выражение: ')

if '+' in math:
    num=math.split('+')
    print(math, '=', int(num[0])+int(num[1]))
if '-' in math:
     num = math.split('-')
     print(math, '=', int(num[0]) - int(num[1]))
if '*' in math:
     num = math.split('*')
     print(math, '=', int(num[0]) * int(num[1]))
if '/' in math:
     num = math.split('/')
     print(math, '=', int(num[0]) / int(num[1]))
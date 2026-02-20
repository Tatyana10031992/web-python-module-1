"""
ЗАДАЧА: Умный контроль доступа (бейджи)

Даны записи содержащие журнал проходов сотрудников.

Каждая строка файла имеет формат:
дата,имя,действие

Где:
- дата     — строка в формате YYYY-MM-DD
- имя      — имя человека
- действие — ENTER (вход) или EXIT (выход)

Журнал проходов:
2026-02-01,Иван,ENTER
2026-02-01,Мария,ENTER
2026-02-01,Иван,EXIT
2026-02-01,Иван,EXIT
2026-02-01,Олег,EXIT
2026-02-02,Мария,EXIT
2026-02-02,Олег,ENTER

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Записать проходы в файл access.log

2. Прочитать файл access.log и загрузить данные.

3. Для каждого человека:
   - посчитать количество входов (ENTER)
   - посчитать количество выходов (EXIT)
   - определить, находится ли человек ВНУТРИ в конце лога
     (ENTER без последующего EXIT)

4. Найти людей с ошибками доступа:
   - EXIT без предварительного ENTER
   - два ENTER подряд без EXIT
   (сохранить таких людей в множество)

5. Для каждой даты посчитать количество входов (ENTER).

6. Найти дату с максимальным количеством входов.

7. Записать подробный отчёт в файл access_report.txt.
"""

f = [
    "2026-02-01,Иван,ENTER",
    "2026-02-01,Мария,ENTER",
    "2026-02-01,Иван,EXIT",
    "2026-02-01,Иван,EXIT",
    "2026-02-01,Олег,EXIT",
    "2026-02-02,Мария,EXIT",
    "2026-02-02,Олег,ENTER",
]

with open("access.log", "w", encoding="utf-8") as file:
    for line in f:
        file.write(line + "\n")

events = []

with open("access.log", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line:
            date, name, action = line.split(",")
            events.append((date, name, action))

stats = {}
inside = {}
errors = set()
daily_enters = {}


for date, name, action in events:
    stats.setdefault(name, {"ENTER": 0, "EXIT": 0})
    inside.setdefault(name, False)
    daily_enters.setdefault(date, 0)

    if action == "ENTER":
        if inside[name]:
            errors.add(name) 
        inside[name] = True
        stats[name]["ENTER"] += 1
        daily_enters[date] += 1
    else:  
        if not inside[name]:
            errors.add(name) 
        inside[name] = False
        stats[name]["EXIT"] += 1

max_day = None
max_enters = 0
for date, count in daily_enters.items():
    if count > max_enters:
        max_day = date
        max_enters = count

with open("access_report.txt", "w", encoding="utf-8") as report:
    report.write("Отчёт по журналу доступа\n\n")

    report.write("Статистика по сотрудникам:\n")
    for name, data in stats.items():
        status = "Внутри" if inside.get(name, False) else "Не внутри"
        report.write(f"- {name}: ENTER={data['ENTER']}, EXIT={data['EXIT']}, Статус: {status}\n")

    report.write("\nСотрудники с ошибками доступа:\n")
    if errors:
        for name in sorted(errors):
            report.write(f"- {name}\n")
    else:
        report.write("Ошибок не выявлено\n")

    report.write("\nКоличество входов по датам:\n")
    for date in sorted(daily_enters.keys()):
        report.write(f"- {date}: {daily_enters[date]}\n")

    report.write(f"\nДата с максимальным количеством входов: {max_day} ({max_enters} входов)\n")

print("Отчёт успешно создан в файле 'access_report.txt'")
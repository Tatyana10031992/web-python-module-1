lines = [
    "Понедельник,09:00,Группа1,Математика,101",
    "Понедельник,09:00,Группа2,Физика,101",
    "Понедельник,10:30,Группа1,Физика,102",
    "Понедельник,12:00,Группа3,История,103",
    "Вторник,09:00,Группа1,Информатика,101",
    "Вторник,09:00,Группа2,Математика,102",
    "Вторник,10:30,Группа3,Физика,101",
    "Вторник,12:00,Группа1,История,103",
    "Среда,09:00,Группа2,Информатика,101",
    "Среда,10:30,Группа3,Математика,101",
    "Среда,10:30,Группа1,Физика,101"
]

schedule = []
group_subjects = {}
group_lesson_count = {}
room_usage = {}
day_lesson_count = {}
conflicts = []  

with open("schedule.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line + "\n")

with open("schedule.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        day, time, group, subject, room = line.split(",")
        lesson = {
            "day": day,
            "time": time,
            "group": group,
            "subject": subject,
            "room": room
        }
        schedule.append(lesson)

for lesson in schedule:  
    day = lesson["day"]
    time = lesson["time"]
    group = lesson["group"]
    subject = lesson["subject"]
    room = lesson["room"]

   
    if group not in group_subjects:
        group_subjects[group] = set()
    group_subjects[group].add(subject)

    group_lesson_count[group] = group_lesson_count.get(group, 0) + 1


    day_lesson_count[day] = day_lesson_count.get(day, 0) + 1

    key = (day, time, room)
    if key not in room_usage:
        room_usage[key] = []
    room_usage[key].append(group)


for key, groups in room_usage.items():
    if len(groups) > 1:
        conflict_info = {
            "day": key[0],
            "time": key[1],
            "room": key[2],
            "groups": groups
        }
        conflicts.append(conflict_info)  


busiest_day = None
max_lessons = 0
for day, count in day_lesson_count.items():
    if count > max_lessons:
        max_lessons = count
        busiest_day = day

with open("schedule_report.txt", "w", encoding="utf-8") as report:
    report.write("Статистика по группам:\n") 
    for group, subjects in group_subjects.items():
        count_lessons = group_lesson_count.get(group, 0)
        subjects_list = ', '.join(sorted(subjects)) 
        report.write(f"- {group}: изучает {subjects_list}, всего занятий: {count_lessons}\n")
    
    report.write("\nКонфликты аудитории:\n")
    if conflicts:  
        for conf in conflicts:
            report.write(f"- День: {conf['day']}, Время: {conf['time']}, Аудитория: {conf['room']}, группы: {', '.join(conf['groups'])}\n")
    else:
        report.write("Конфликтов нет.\n")

    if busiest_day:
        report.write(f"\nДень с максимальной нагрузкой: {busiest_day} (занятий: {max_lessons})\n")
    else:
        report.write("\nРасписание пустое, нет дней с занятиями.\n")

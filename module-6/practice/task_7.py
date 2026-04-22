import random
tasks = []

for i in range(10):
    tasks.append({
        "id": f"t_{i}",
        "assignee": random.choice(["ivan", "olga", "petr", "anna", "oleg"]),
        "status": random.choice(["in_progress", "blocked", "in_review", "waiting_vendor"]),
        "days_in_status": random.randint(0, 10)

    })
# for task in task:
#     print(t)
# print()

# in_progress_long = set()
# for t in task:
#     if t["status"] == "in_progress" and t["days_in_status"] > 7:
#         in_progress_long.add(t["assignee"])  

# print(list(in_progress_long) if in_progress_long else "Не найдено")
# print()


status_asignees ={}
for task in tasks:
    status = task["status"]
    asignees = task["assignee"]
    if status not in status_asignees:
        status_asignees[status]=set()
    status_asignees[status].add(asignees)
 
result={}

for status in status_asignees:
    if len (status_asignees[status]) == 1:
        result[status]=list(status_asignees[status])[0]

print(result)
    
max_days = 0
assignee = None
for task in tasks:
    if task["status"] == "in progress" or task["status"] == "blocked":
        if task["days_in_status"] > max_days:
            max_days = task["days_in_status"]
            assignee = task["assignee"]
print(f"{assignee}: {max_days}")



    







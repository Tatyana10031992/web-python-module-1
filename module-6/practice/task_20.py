logs = [
    ("ivan", 8),
    ("ivan", 10),
    ("olga", 20),
    ("petr", 45),
]

hours_total = {}

for employee, hours in logs:
    hours_total[employee] = hours_total.get(employee, 0) + hours
    
overtime = [employee for employee, total_hours in hours_total.items() if total_hours > 40 ]
underwork = [employee  for employee, total_hours in hours_total.items() if total_hours < 20]

for employee, total_hours in hours_total.items():
    print(f"{employee }: {total_hours}")
    
for employee in overtime:
    print(employee)
    
for employee in underwork:
    print(employee)

logs = [
    ("ivan", "d1", "login"),
    ("ivan", "d1", "view"),
    ("ivan", "d2", "login"),
    ("olga", "d1", "login"),
    ("petr", "d2", "error"),
    ("anna", "d1", "login"),
    ("anna", "d2", "view"),
]

user_action_count = {}
user_actions = {}
user_days = {}
day_activity = {}

for user, day, action in logs:
    user_action_count[user] = user_action_count.get(user, 0) + 1

    if user not in user_actions:
        user_actions[user] = set()
    user_actions[user].add(action)
        
    if user not in user_days:
        user_days[user] = set()
    user_days[user].add(day)
    
    if day not in day_activity:
        day_activity[day] = set()
    day_activity[day].add((user, action))

day_activity_counts = {day: len(actions) for day, actions in day_activity.items()}

min_activity_day = min(day_activity_counts, key=day_activity_counts.get)
min_activity_count = day_activity_counts[min_activity_day]

error_user = set()
for user, actions in user_actions.items():  
    if "error" in actions and "login" not in actions:
        error_user.add(user)

user_multiple_days = set()
for user, days in user_days.items():  
    if len(days) > 1:
        user_multiple_days.add(user)

report = {
    "user_action_count": user_action_count,
    "error_user": error_user,
    "user_multiple_days": user_multiple_days,
    "day_with_min_activity": min_activity_day,
    "min_activity_count": min_activity_count, 
}



print(user_action_count)
print(error_user)
print(user_multiple_days)  
print(min_activity_day)
print(min_activity_count)

for key, value in report.items():
    print(f"{key}: {value}")

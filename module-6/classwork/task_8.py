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
user_action = {}
user_days = {}


for user,day,action in logs:
    user_action_count[user] = user_action_count.get(user, 0) + 1


    if user not in user_action:
        user_action [user] = set() 
    user_action[user].add(action)
        
    if user not in user_days:
            user_days[user] = set()
    user_days[user].add(day)

error_user = set()
for user, action, in user_action.items():
    if "error" in action and "login" not in action:
        error_user.add(user)

user_days_more_one = set()
for user, day in user_days.items():
    if len(day) > 1:
        user_days_more_one.add(user)


print(user_action_count)
print(user_action)
print(user_days_more_one)





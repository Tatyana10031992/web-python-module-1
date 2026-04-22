payments = [
    ("ivan", 100),
    ("ivan", -30),
    ("ivan", -20),
    ("olga", 200),
    ("petr", -50),
]

balances = {}
operations_count = {}

for user, amount in payments:
    balances[user] = balances.get(user, 0) + amount
    operations_count[user] = operations_count.get(user, 0) + 1


negative_balances = [user for user, balance in balances.items() if balance < 0]
more_than_two_ops = [user for user, count in operations_count.items() if count > 2] 


for user, balance in balances.items():
    print(f"{user}: {balance}")


for user in negative_balances:
    print(user)

for user in more_than_two_ops:  
    print(user)

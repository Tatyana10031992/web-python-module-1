purchases = [
    {"user": "Алиса", "items": ["яблоко", "банан"],          "price": 120, "timestamp": 1},
    {"user": "Боб",   "items": ["банан"],                    "price": 50,  "timestamp": 2},
    {"user": "Алиса", "items": ["апельсин", "яблоко"],       "price": 150, "timestamp": 5},
    {"user": "Боб",   "items": ["яблоко", "апельсин"],       "price": 130, "timestamp": 6},
    {"user": "Алиса", "items": ["банан", "банан"],           "price": 70,  "timestamp": 15},
    {"user": "Боб",   "items": ["банан"],                    "price": 40,  "timestamp": 25},
]

purchase_count = {}
total_spent = {}
user_unique_items = {}
user_total_items = {}
item_frequency = {}
user_timestamps = {}

for purchase in purchases:
    user = purchase["user"]
    items = purchase["items"]
    price = purchase["price"]
    timestamp = purchase["timestamp"]
    
   
    purchase_count[user] = purchase_count.get(user, 0) + 1
    total_spent[user] = total_spent.get(user, 0) + price
    
 
    if user not in user_unique_items:
        user_unique_items[user] = set()
    user_unique_items[user].update(items)
    
   
    user_total_items[user] = user_total_items.get(user, 0) + len(items)
   
    for item in items:
        item_frequency[item] = item_frequency.get(item, 0) + 1
    
  
    if user not in user_timestamps:
        user_timestamps[user] = []
    user_timestamps[user].append(timestamp)


most_common_item = max(item_frequency.items(), key=lambda x: x[1])[0]

max_spent_user = max(total_spent.items(), key=lambda x: x[1])[0]

max_items_user = max(user_total_items.items(), key=lambda x: x[1])[0]

max_gaps = {}
for user, timestamps in user_timestamps.items():
    timestamps.sort()
    max_gap = 0
    for i in range(1, len(timestamps)):
        gap = timestamps[i] - timestamps[i - 1]
        if gap > max_gap:
            max_gap = gap
    max_gaps[user] = max_gap


print("Общее количество покупок каждого пользователя:", purchase_count)
print("Общая сумма, потраченная каждым:", total_spent)
print("Множество уникальных товаров каждого:", user_unique_items)
print("Общее количество товаров каждого:", user_total_items)
print("Самый популярный товар:", most_common_item)
print("Частоты товаров:", item_frequency)
print("Массив timestamp каждого пользователя:", user_timestamps)
print("Максимальные интервалы между покупками по пользователям:", max_gaps)
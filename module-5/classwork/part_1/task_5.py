clients = [
    (1, "111", "a@x.com"),
    (2, "111", "b@x.com"),
    (3, "222", "c@x.com"),
    (4, "333", "c@x.com"),
    (5, "444", "d@x.com"),
]



phones = {}
emails = {}
for id, number, email in clients:
    phones.setdefault(number, set()).add(id)
    emails.setdefault(email, set()).add(id)
print(clients)


dublicates = []
for o in (phones, emails):
    for ids in o.values():
        if len(ids) > 1:
            dublicates.append(ids)
print(dublicates)

dublicates_ids = set()
for m in dublicates:
    dublicates_ids  |= m

clean_clients = []
for client in clients:
    if client[0] not in dublicates_ids:
        clean_clients.append(client[0])
print(clean_clients)




        

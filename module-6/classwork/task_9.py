"""
ЗАДАЧА: Анализ чатов пользователей

Даны сообщения в чате. Каждое сообщение представлено словарём
со следующими ключами:
- "user"      : имя пользователя (строка)
- "text"      : текст сообщения (строка)
- "timestamp" : время сообщения (целое число, возрастает не строго)

Пример входных данных:
messages = [
    {"user": "Алиса", "text": "привет здравствуй",     "timestamp": 1},
    {"user": "Боб",   "text": "здравствуй",            "timestamp": 2},
    {"user": "Алиса", "text": "как дела у тебя",       "timestamp": 3},
    {"user": "Боб",   "text": "привет Алиса",          "timestamp": 4},
    {"user": "Алиса", "text": "привет привет здравствуй", "timestamp": 10},
    {"user": "Боб",   "text": "пока",                  "timestamp": 20},
]

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Посчитать количество сообщений каждого пользователя.
   Результат сохранить в словарь вида:
   {
       "Алиса": 3,
       "Боб": 2
   }

2. Для каждого пользователя:
   2.1 Найти множество уникальных слов, которые он использовал
       (слова разделяются методом split()).
   2.2 Найти самое частое слово пользователя.
       Если самых частых слов несколько — можно выбрать любое.

3. Найти пользователя с самым большим словарным запасом,
   где словарный запас — это количество уникальных слов,
   использованных пользователем.

4. Найти множество слов, которые использовали ВСЕ пользователи
   (пересечение множеств слов пользователей).

5. Для каждого пользователя определить максимальный перерыв
   между его сообщениями:
   - перерыв = разница между timestamp текущего и предыдущего сообщения
   - найти пользователя с самым большим таким перерывом
"""



messages = [
    {"user": "Алиса", "text": "привет здравствуй",     "timestamp": 1},
    {"user": "Боб",   "text": "здравствуй",            "timestamp": 2},
    {"user": "Алиса", "text": "как дела у тебя",       "timestamp": 3},
    {"user": "Боб",   "text": "привет Алиса",          "timestamp": 4},
    {"user": "Алиса", "text": "привет привет здравствуй", "timestamp": 10},
    {"user": "Боб",   "text": "пока",                  "timestamp": 20},
]

messages_count = {}
user_words = {}
frq_words = {}
most_frq = {}
max_breaks = {}




for message in messages:
    user = message["user"]
    messages_count[user] = messages_count.get(user, 0) + 1

    user = message["user"]
    words = message["text"].split()

    if user not in user_words:
        user_words[user] = set()
    user_words[user].update(words)

for user_name in user_words:
    for message in messages:
        if message["user"] == user_name:
            for word in message["text"].split():
                frq_words[word] = frq_words.get(word, 0) + 1

        
    
    max_word = None
    max_count = 0
    for word, count in frq_words.items():
        if count > max_count:
            max_count = count
            max_word = word
        most_frq[user_name] = max_word

        
    
    
max_user_name = None
max_len = 0

for user, words in user_words.items():
    if len(words) > max_len:
        max_user_name = user
        max_len = len(words)
if max_user_name != None:
    print(max_user_name)


common_words = set.intersection(*user_words.values())



    



print(messages_count)
print(user_words)
print(frq_words)
print(most_frq)
print(common_words)





    
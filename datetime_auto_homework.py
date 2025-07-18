'''
Наше домашнє завдання полягає в наступному. У межах вашої організації,
ви відповідаєте за організацію привітань колег з днем народження.
Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays,
яка допоможе вам визначати, кого з колег потрібно привітати.
 Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.

У вашому розпорядженні є список users,
кожен елемент якого містить інформацію про ім'я користувача та його день народження.
Цей список виглядає наступним чином.

users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "Sarah Lee", "birthday": "1957.3.23"},
    {"name": "Jonny Lee", "birthday": "1958.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
Оскільки дні народження колег можуть припадати на вихідні,
 ваша функція також повинна враховувати це та переносити
 дату привітання на наступний робочий день, якщо це необхідно.
'''



'''
На першому кроці ми виконаємо роботу з датами. 
Мета кроку це ознайомлення з базовими операціями над датами які нам знадобляться для цієї задачі.

Напишіть функцію string_to_date, 
яка приймає рядкове представлення дати в форматі "YYYY.MM.DD" і перетворює його на об'єкт datetime.date.

Напишіть зворотну функцію date_to_string, 
яка приймає об'єкт datetime.date і повертає рядкове представлення дати в форматі "YYYY.MM.DD".

Ці функції повинні працювати наступним чином:

date_string = "2024.01.01"
converted_date = string_to_date(date_string)
print(converted_date)
date_string = date_to_string(converted_date)
print(date_string)
Виконання такого коду призведе до наступного виведення:

2024-01-01
2024.01.01
'''
from datetime import datetime
def string_to_date (string_date:str)-> datetime.date:
    converted_date = datetime.strptime(string_date,'%Y.%m.%d')
    return converted_date.date()
#print(string_to_date("2024.01.01"))

def date_to_string(converted_date:datetime.date) -> str:
    date_string = converted_date.strftime('%Y.%m.%d')
    return date_string
#print(date_to_string(string_to_date("2024.01.01")))



'''
На другому кроці ми виконаємо операції над списками користувачів. 
Мета кроку це навчитися працювати зі списками та словниками в Python в межах нашого завдання.

Напишіть функцію prepare_user_list, яка приймає список імен користувачів 
та їх дат народження у рядковому форматі, і повертає список словників
 у форматі {"name": <name>, "birthday": <birthday>}, де <birthday> - це об'єкт datetime.date.

Виконання наступного коду для вашої функції:

users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

prepared_users = prepare_user_list(users)
print(prepared_users)
Повинно призводити до виведення:

[
    {"name": "Bill Gates", "birthday": datetime.date(1955, 3, 25)},
    {"name": "Steve Jobs", "birthday": datetime.date(1955, 3, 21)},
    {"name": "Jinny Lee", "birthday": datetime.date(1956, 3, 22)},
    {"name": "John Doe", "birthday": datetime.date(1985, 1, 23)},
    {"name": "Jane Smith", "birthday": datetime.date(1990, 1, 27)},
]

Як бачимо, після виконання функції, в словнику значення ключа "birthday" 
має бути об'єктом datetime.date. Для перетворення рядка в об'єкт datetime.date 
використовуйте написану на першому кроці функцію string_to_date, 
яка приймає рядкове представлення дати в форматі "YYYY.MM.DD" 
і перетворює його на об'єкт datetime.date.


'''
users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
def prepare_user_list(user_data:str)->list:
        prepared_users = []
        for user in users:
            new_user = {'name': user['name'], 'birthday': string_to_date(user['birthday']) }
            prepared_users.append(new_user)
        return prepared_users
#print(prepare_user_list(users))
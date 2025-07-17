#Наприклад ми хочемо визначити скільки пройшло повних днів,
#коли Наполеон спалив Москву, а це відбулося 14 вересня 1812 року


from datetime import datetime

napoleon_burns_moscow = datetime(year = 1812, month = 9, day = 14)
today = datetime.now()

result = today.toordinal() - napoleon_burns_moscow.toordinal()

print(result)





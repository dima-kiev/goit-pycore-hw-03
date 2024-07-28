from datetime import datetime, timezone, timedelta

FORMAT = '%YYYY-%mm-%dd'


def get_days_from_today(date: str):
    try:
        parsed_date = datetime.strptime(date, FORMAT)
    except ValueError:
        print("Wrong date format " + date + ". Expected to be like  " + FORMAT)
        exit(-1)
    return (datetime.today() - parsed_date).days


date_in_the_past = datetime(year=1976, month=7, day=11).strftime(FORMAT)
date_in_the_future = datetime(year=2976, month=7, day=11).strftime(FORMAT)

print(get_days_from_today(date_in_the_past))
assert get_days_from_today(date_in_the_past) > 0

print(get_days_from_today(date_in_the_future))
assert get_days_from_today(date_in_the_future) < 0

get_days_from_today("1999 JAN 01")


#Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

#Вимоги до завдання:

#Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
#Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної.
# Якщо задана дата пізніша за поточну, результат має бути від'ємним.
#У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
#Для роботи з датами слід використовувати модуль datetime Python.


#Рекомендації для виконання:

#Імпортуйте модуль datetime.
#Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
#Отримайте поточну дату, використовуючи datetime.today().
#Розрахуйте різницю між поточною датою та заданою датою.
#Поверніть різницю у днях як ціле число.

#Критерії оцінювання:

#Коректність роботи функції: функція повинна точно обраховувати кількість днів між датами.
#Обробка винятків: функція має впоратися з неправильним форматом вхідних даних.
#Читабельність коду: код повинен бути чистим і добре документованим.

#Приклад:

#Якщо сьогодні 5 травня 2021 року, виклик get_days_from_today("2021-10-09") повинен повернути 157,
# оскільки 9 жовтня 2021 року є на 157 днів пізніше від 5 травня 2021 року.
import datetime

# ввод даты рождения
day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения: "))
year = int(input("Введите год рождения: "))

birth_date = datetime.date(year, month, day)

# определяем день недели
print("День недели:", birth_date.strftime("%A"))

# проверяем високосный год
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Год был високосный")
else:
    print("Год не был високосным")

# правильный расчет возраста
today = datetime.date.today()

age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print("Ваш возраст:", age)

# вывод даты звездочками
date_str = f"{day:02d}{month:02d}{year}"

print("\nДата звездочками:")

for digit in date_str:
    print("*" * int(digit))
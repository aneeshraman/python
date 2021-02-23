from datetime import date

year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))

birth_date = date(year, month, day)

today_date = date.today()

age = today_date - birth_date

print(age.days)
a = input()

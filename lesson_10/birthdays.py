import random
import datetime

while True:
    number = input("Сколько дней рождения генерируем?(до 70)")
    if  not number.isdigit() or int(number) < 2 or int(number) > 70:
        print("Нужно число от 2 до 70")
        print("-" * 5)
    else:
        number = int(number)
        break #выход из цикла while

brithdays = []
startOfYear = datetime.date(2022, 1, 1)
for _  in range(number):
    sdvig = random.randint(0,364)
    randomDay = datetime.timedelta(sdvig)
    birthday = startOfYear + randomDay
    brithdays.append(birthday)

for index in range(number):
    print(f"{index + 1}){brithdays[index].strftime('%d.%m.%y')}") #strftime поменять формат
print("=" * 10)
for i in set(brithdays): #список -> множество(исключение повторений)
    if brithdays.count(i) > 1:
        print(f" - {i.strftime('%d.%m.%y')}встречается {brithdays.count(i)}раза")





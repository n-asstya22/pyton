#циклы
#while
# x = 10
# while x != 0:
#     print(x)
#     x -= 1            #тоже самое что и х = х - 1
# while True:           #срабатывает каждый раз
#     break             #выйти из while
#
# #for
#
# lst = ["A" , "Б" , "В" , "Г", "Д"]
# for letter in lst:    #проитерироваться по списку
#     print(letter)
# for img in range(0, 3):
#     print(img)

# word = input("Введи слово:")
# while word:           #пока словo не пустое
#     print(word , end=" ")
#     word = word[:-1]

# x = int(input("Введите число:"))
# while x:   #while x != 1 (из-за типа "число")
#     x -= 1
#     if x % 2 == 0:
#         print(x)
x = input("Введите число: ").strip()
if not x.isdigit() or int(x) <= 1 :
    print("Это корявое число,нцжно другое число")
    quit()
else:
    x = int(x)
step = 0

while x != 1:
    step += 1
    if x % 2 == 0:
        print(f"{step})", end=" ")
        print(x, " x // 2 =" , end=" ")
        x = x // 2

    else:
        print(f"{step})", end=" ")
        print(x, "x * 3 + 1 =", end=" ")

        x = x * 3 + 1
    print(x)
print("Шагов" , step)

# x1 = int(input("Число :"))
# x2 = int(input("Число :"))
# #
# # while x1 <= x2:
# #     print(x1)
# #     x1 += 1 #тоже самое что и х1 = х1 + 1
#
# for peremenaya in range(x1, x2+1) :
#     print(peremenaya)

while True:
    try:
        level = int(input("Сколько уровней будет в елочке?"))
    except ValueError: #букву в число
        print("надо число ")
        continue # перезапуск while
    else:  #если ошибок нетrue
        break # выход из while True

while True:
    char = input("Какой символ?").strip()
    if len(char) == 1 :
        break

for i in range(1, level + 1): #от 1 до левла + 1
    #левач половина
    print(" " * (level-i), end= "")
    print(char * i , end="")

    #правая половина
    print( char * i )
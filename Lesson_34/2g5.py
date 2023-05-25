import random
######ex3
####i = input("Введите число: ")
##i_list = i.split(".")
##if len(i_list) == 1:
##    i = int(i_list[0])
##elif len(i_list) == 2:
##    i = int(i_list[0]) + 1
##
##print(i)
##
####ii = float(i)
####iii = round(ii)
####print(iii)
######ex4
##al =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
##       's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
##i = int(input())
##st = ""
##se = set()
##for b in range(i + 1):
##    e = random.choice(al)
##    st = st + e
##se = set(st)
##
##
##print(st)
##print(se)
######ex5
while True:
    a = input("Введите текст: ")
    if "Суета" in a:
        if "Суетолог" not in a:
            break
        else:
            True
    else:
            True

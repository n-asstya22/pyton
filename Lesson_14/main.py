# # Задача 1
#
# phrase = "Россия, Россия, Россия!".title().strip
# print(phrase)
# s = list("1234567890!№;%:?*().,*/\"@#$%^1&")
# phrase_clear =""
#
# for _ phrase:
#     if phrase not in s:
#         phrase_clear += _
#
# phrase_list = phrase_clear.split(" ")
# print(phrase_list)
#
# d = {}
# for dom in phrase_list:
#     if dom not in d:
#         d[dom] = 1
#     else:
#         dom += 1
# print(d)P
# Задача 2
# slu = 0
# d = {"Молоко" : 70,
#      "Доширак" : 30,
#      "Чипсы" : 80,
#      "Сок" : 40}
# for i in d.values():
#     slu += i
#
# print(slu)
#Задача 3
die_sides = 6
die_count = 2
d = []
for first in range(1, die_sides + 1):
    for second in range(1, die_sides + 1):
        if first + second not in d:
            first + second += [(first, second)]
        else:
            d[first + second].append(first, second)
 #вывод
for t in d:
    print(f"{t}:{d[t]}")



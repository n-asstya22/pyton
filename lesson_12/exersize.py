# a = int(input("Число: "))
# b = int(input("Число: "))
# lst = []
#
# for _ in range(a + 1, b):
# print(lst)
#     lst.append( _ ** 2)
#


lst = [-5, 14, 2, -8, 1]
mini = min(lst)
maхi = max(lst)

lst[lst.index(mini)], lst[lst.index(maхi)] = lst[lst.index(maхi)], lst[lst.index(mini)]
print(lst)

a = input()
b = set(a) #чтобы убрать поторяющиеся символы
c = len(b)

if c % 2 == 1:
    print("IGNORE HIM!")
elif c % 2 == 0:
    print("CHAT WITH HER!")

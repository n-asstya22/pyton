input()
a = input()
perexod = 0
uberaem = 0
while len(a) - 1 != perexod:
    if a[perexod] == a[perexod+1]:
        a = a[:perexod]+a[perexod+1:]
        uberaem += 1
    else:
        perexod += 1

print(uberaem)
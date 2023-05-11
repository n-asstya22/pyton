n = int(input())
g = 0
for i in range(n):
    a = input()
    list = a.split(" ")
    b = int(list[0])
    c = int(list[1])
    d = int(list[2])
    if b + c + d > 1:
        g += 1
print(g)





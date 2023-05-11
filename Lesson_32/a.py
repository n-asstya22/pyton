a1 = input().lower()
a2 = input().lower()
b = 0
for i in range(len(a1)):
    if a1[i] != a2[i]:
        if a1[i] < a2[i]:
            b = -1
        elif a1[i] > a2[i]:
            b += 1
            break

print(b)




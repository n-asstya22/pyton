x = 0
n = int(input())
for i in range(n):
    b = input()
    if b == "++X" or b == "X++":
        x += 1
        
    elif b == "--X" or b == "X--":
        x -= 1
print(x)

#beens
beans = 20
def vichitanie(x):
    global beans
    beans -= x


while beans > 0:
    while True: #валидация(не трогать)
        x1 = int(input("Первый игрок,Сколько фасолин взять:"))
        if x1 < 4 and 0 < x1:
            break
    vichitanie(x1)
    print(beans)
    if beans <= 0:
        print("ПОБЕДИЛ ВТОРОЙ ИГРОК")
        break

    while True: #валидация(не трогать)
        x2 = int(input("Второй игрок,Сколько фасолин взять:"))
        if x2 < 4 and 0 < x2:
            break
    vichitanie(x2)
    print(beans)
    if beans <= 0:
        print("ПОБЕДИЛ ПЕРВЫЙ ИГРОК")
        break


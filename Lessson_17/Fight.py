from random import randint
import time
print("Время проверить твою ловкость и скорость и понять, кто самый быстрый стрелок на западе! Когда увидишь 'СТРЕЛЯЙ', у тебя будет 0.3 секунды чтобы нажать Enter. Но если ты нажмёшь Enter раньше, то ты проиграл.")

input("нажми Enter,чтобы начать:")
print("Время пострелять")
time.sleep(randint(2,5))
start = time.time()
input("Стреляй!!")
end = time.time()
delta = end - start
print(delta)
if delta > 0.3:
    print("Ты проиграл🐢🐌")
elif delta < 0.001:
    print("Ты слишком быстрый")
else:
    print("Ты выйграл😎")


    
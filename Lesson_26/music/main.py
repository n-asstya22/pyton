from m_b import Musicbox
a = Musicbox()  # mp3-player
while True:
    a.playing()
    user = input("Что ты сейчас услышал? ").lower()
    if user == "":  #если ответ пустой
        break
    a.cheak(user)

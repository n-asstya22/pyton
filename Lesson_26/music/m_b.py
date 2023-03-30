import random
import playsound
class Musicbox:
    def __init__(self):
        self.variants = "abvgon"  # варианты угадываемых звуков
        self.score = 0  # счет
        self.sequence = random.choice(self.variants)  # последовательность
    def __next_lvl(self):
        # self.sequence += random.choice(self.variants)  # + одна буква к последоватеьности
        dlina = len(self.sequence) + 1
        self.sequence = ""
        for _ in range(dlina):
            self.sequence += random.choice(self.variants)

    def cheak(self,ans):
        if ans == self.sequence:
            self.score += 1
            playsound.playsound('sounds/correct.wav')
            self.__next_lvl()
        else:
            self.score += 0.5
            playsound.playsound('sounds/incorrect.wav')

    def playing(self):
        for letter in self.sequence:
            playsound.playsound(f'sounds/{letter}.mp3')







import random
import hangman_art as art

print(art.intro)

vocabulary = ['Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty', 'Natasha', 'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill']

word_answer = random.choice(vocabulary)

word_display = []
for _ in range(len(word_answer)):
    word_display.append("_")
#print(word_answer)

print(word_display)
life = 6
counter = 0


while life > 0 and counter != len(word_answer):
    print(art.stages[life])
    letter_is_be = False
    letter = input("Буква:").lower()
    for i in range(len(word_answer)): #пробегаемся по ответу
        if letter == word_answer[i]:
            if word_display[i] != "_" :
                letter_is_be = True
            else:
                word_display[i] = letter
                counter +=1
                letter_is_be = True
    if not letter_is_be: #если мимо
        life -= 1
    print(word_display)

if counter == len(word_answer):
    print("Победа")
else:
    print(art.stages[life])
    print("Не получилось")
    print(word_answer)



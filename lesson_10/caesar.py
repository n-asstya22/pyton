alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'img', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
should_end = False
symbols = [" ", ".", ",", ")", "(", "-", "+" ]

while should_end == False:
    text = input("Сообщение:").lower()
    text = list(text) #из строки в спиок

    shift = int(input("Сдвиг:"))
    if shift > len(alphabet):
        shift = shift % len(alphabet)
    elif shift < -len(alphabet):
        shift = shift % -len(alphabet)
#механизм сдвига
    cipher_text = ""
    for letter in text:
        if letter in symbols:
            cipher_text += letter
        else:
            position = alphabet.index(letter)
            if position + shift > len(alphabet):
                new_position = position + shift - len(alphabet)
            elif position + shift < 0:
                new_position = position + shift + len(alphabet)
            else:
                new_position = position + shift
            cipher_text += alphabet[new_position]
    print(cipher_text)



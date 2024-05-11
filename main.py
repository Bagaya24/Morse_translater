alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


morse_alphabet = ['._', '_..', '_._.', '_..', '.', '.._.', '__.', '....', '..', '.___', '_._', '._..', '__', '_.',
                  '___', '.__.', '__._', '._.', '...', '_', '.._', '..._', '.__', '_.__', '__..']

morse_number = ['_____', '.____', '..___', '...__', '...._', '.....', '_....', '__...', '___..', '____.']


welcome_logo = """"""
buy_logo = """"""


def alphanum_to_morse(sent):
    morse_list = []

    for word in sent:

        if word in alphabet:
            word_index = alphabet.index(word)
            morse_words = morse_alphabet[word_index]

            morse_list.append(morse_words)
        elif word in number:
            number_index = number.index(word)
            morse_nb = morse_number[number_index]
            morse_list.append(morse_nb)
    return " ".join(morse_list)


def morse_to_alphanum(sent):
    alphanum_list = []
    for word in sent.split():
        if word in morse_alphabet:
            index_morse_alpha = morse_alphabet.index(word)
            alpha_word = alphabet[index_morse_alpha]
            alphanum_list.append(alpha_word)
        elif word in morse_number:
            index_morse_num = morse_number.index(word)
            num_word = number[index_morse_num]
            alphanum_list.append(num_word)

    return "".join(alphanum_list)


while True:
    print('------------------------Welcome to The Morse Translater-------------------------------')
    choice = input("Type '1' to translate alpha numeric to morse and '2' to translate morse to alpha numeric: ")

    if choice == '1':
        sentence = input("Enter an sentence: ").lower()
        morse_sentence = alphanum_to_morse(sentence)
        print(morse_sentence)
    elif choice == '2':
        sentence = input("Enter an sentence: ").lower()
        alphanum_sentence = morse_to_alphanum(sentence)
        print(alphanum_sentence)
    else:
        continue

    translate_again = input("Do you want to translate again? Type 'y' to continue and 'n' to stop: ").lower()
    if translate_again == 'n':
        print("See you soon")
        break

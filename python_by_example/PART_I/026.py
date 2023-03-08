word = input("Input a word: ")
first_letter = word[0]
rest_word = word[1:]
if first_letter != 'a' and first_letter != 'e' and first_letter != 'y' and first_letter != 'u' and first_letter != 'i' and first_letter != 'o' : print(
        rest_word + first_letter + "ay"
    )
else:
    print(word + 'way')

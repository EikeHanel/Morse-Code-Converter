# TODO
#   1. Get a Json/Dictionary for the ABC to Morse Code
#   2. Create input for the word that should be converted.
#   3. Convert the word.
#   4. Give an output

from morse_code import morse_code


def str_to_morse_code(word_string):
    word_in_morse = ""
    for letter in word_string:
        if letter not in morse_code.keys():
            word_in_morse += "#"
        else:
            word_in_morse += morse_code[letter] + " "
    print(f"Your word '{word_string}' has been converted into Morse code as: {word_in_morse}")


print("Welcome to the Morse Code Converter!\nIf your input is a charter that is not a supported, "
      "a '#' will be shown in its place.")

run = True
while run:
    word = input("Type the word that you want converted: ").lower()
    str_to_morse_code(word)

    again = input("Want to convert another word? Type Y/N: ").lower()
    if again == "n":
        run = False
    elif again != "n" and again != "y":
        print("Input was not clear program is being closed!")
        run = False

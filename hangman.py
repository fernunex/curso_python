import unidecode
import random
import os


def read_words():
    """This function read data form a file.
    For this game the words in the file must be one word per line
    Example: 
    Car
    Helicopter
    etc.
    """
    with open("./archivos/data.txt", "r") as f:
        words = f.readlines()

    # print(words)
    return words


def choose_a_word(list_of_words):
    """This function select a word from a list of words.
    exampel = ['dog','car','juan']

    Args:
        list_of_words (list): needs to be a list of words.

    Returns:
        str: a  string like 'cat', etc.
    """
    # Generating a random number to choose a word from the list words
    n_words = len(list_of_words)
    n = random.randint(0, n_words)
    chose_word_accent = list_of_words[n-1].strip()
    chose_word = unidecode.unidecode(chose_word_accent).upper()
    # print(n_words)
    # print(n)
    # print(choosed_word)

    return chose_word


def comparision_words(word_selected, lives):
    """This function creates a dictionary using a string. The keys are the 
    numbers 0,1,2,etc (int) with the same longitude like the word to convert in a
    dictionary. The values are every single letter of the word.
    Additionaly creates a dictionary with the same key but the values '_' initialy.    

    Args:
        word_selected (string): just alpha
        lives (int): Just need to be a integer positive number (between 0 - 9)

    Raises:
        ValueError: if the 'letters' introduced are not letter, then raises a ValueError
    """
    len_word = len(word_selected)

    # Converting word_selected to a dict
    dict_word = {}
    i = 0
    for word in word_selected:
        dict_word[i] = word
        i += 1
    # print(dict_word)

    # Creating a dict empty ("_") for adding words
    dict_comparision = {i: "_" for i in range(len_word)}

    # print(dict_comparision)

    while dict_word != dict_comparision:
        print("\nGuess the word\n")
        for value in dict_comparision.values():
            print(f"{value}", end=" ")
        print("\n")

        # Getting a letter from input
        while True:
            try:
                letter_introduced = input("Enter a letter: ").upper()
                if letter_introduced.isalpha() and len(letter_introduced) == 1:
                    break
                raise ValueError
            except ValueError:
                print("Please enter letter")
        os.system("clear")

        # Checking if the letter is in the word
        if letter_introduced in dict_word.values():
            dict_comparision = dict_comparision | {i: letter_introduced for i in range(
                len_word) if letter_introduced == dict_word[i]}
            print(f"Well done       lives:", lives*"♥ ")
            continue
        else:
            print(f"oops, the {letter_introduced} is not in the word :C")
            if lives == 0:
                continue

        # If the letter is not in the word selected, then -1 life
        lives -= 1
        print(f"Now you have {lives} lives", lives*"♥ ")
        if lives < 1:
            print("You are dead, max lives limit reached!")
            won = False
            break
        won = True

    if won:
        os.system("clear")
        print("Well done the word is:")
        for value in dict_comparision.values():
            print(f"{value}", end="")
    else:
        os.system("clear")
        print("OOPS, the word was:")
        for value in dict_word.values():
            print(f"{value}", end="")


def run():
    playing = 'y'

    while playing == 'y':
        set_1_words = read_words()
        word_select = choose_a_word(set_1_words)
        os.system("clear")
        print("*** Welcome to HANGMAN GAME **")
        print("Enter how many lives you want 0(infinites) - 9")
        level = 0
        while True:
            try:
                level = int(input(": "))
                if level < 0 or level > 9:
                    raise ValueError

            except ValueError:
                print("Please enter a number between 0 - 9")

            else:
                if level == 0:
                    print("Now you have infinite lives")
                    break
                print(f"Now you have {level} lives", level*"♥ ")
                break
        comparision_words(word_select, level)

        print("\n", "_"*20, "\n")
        try:
            playing = input('Do you want to play again? [y/n]')
            if playing.isalpha() and (playing == 'y' or playing == 'n'):
                continue
            raise ValueError
        except ValueError:
            print("Pleas enter 'y' for YES or 'n' for NOT")

    print("Thanks for playing HANGMAN")


if __name__ == "__main__":
    run()

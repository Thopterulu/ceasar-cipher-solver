import argparse
import enchant

DICT = enchant.Dict("en_US")

def check_words(word : str, nb_words : int):
    if DICT.check(word):
        nb_words += 1
    print(word + " ", end="")
    return nb_words

def solve_a_cipher(increment: int, full_string : str):
    nb_words = 0
    word = ""
    for a_char in full_string:
        if a_char == " ":
            nb_words = check_words(word, nb_words)
            # if DICT.check(word):
            #     nb_words += 1
            # print(word + " ", end="")
            word = ""
            continue
        word += chr((ord(a_char) + i)%26+ 97)
    nb_words = check_words(word, nb_words)
    print()
    if nb_words >= 1 :
        print("\n! above it's likely to be the answer !\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("cipher", help="Parse the string you put here")
    pof = parser.parse_args()
    pof.cipher

    full_string = pof.cipher

    for i in range(1, 26):
        solve_a_cipher(i, full_string)

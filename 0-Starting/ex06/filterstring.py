# filterstring.py

import sys
from ft_filter import ft_filter


def main():

    args = sys.argv

    if len(args) != 3:
        print("AssertionError: the arguments are bad")
        return

    try:
        S = str(args[1])
        N = int(args[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    words = S.split()

    clean_words = ft_filter(lambda word: word.isalnum(), words)

    filtered_words = ft_filter(lambda word: len(word) > N, clean_words)

    print(filtered_words)


if __name__ == "__main__":
    main()

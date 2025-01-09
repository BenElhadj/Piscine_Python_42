# building.py

import sys


def main():

    punct = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    if len(sys.argv) == 1:
        text = input("What is the text to count?\n")
    elif len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        print("AssertionError: more than one argument is provided")
        return

    print(f"The text contains {len(text)} characters:")
    print(f"{sum(1 for char in text if char.isupper())} upper letters")
    print(f"{sum(1 for char in text if char.islower())} lower letters")
    print(f"{sum(1 for char in text if char in punct)} punctuation marks")
    print(f"{sum(1 for char in text if char.isspace())} spaces")
    print(f"{sum(1 for char in text if char.isdigit())} digits")


if __name__ == "__main__":
    main()

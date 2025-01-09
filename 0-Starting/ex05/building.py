# building.py

import sys


def main():
    """
    Analyze the given text and count the number of characters,
    uppercase letters, lowercase letters, punctuation marks,
    spaces, and digits.
    """
    punct = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    if len(sys.argv) == 1:
        text = input("What is the text to count?\n")
    elif len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        raise AssertionError("more than one argument is provided")

    print(f"The text contains {len(text)} characters:")
    print(f"{sum(1 for char in text if char.isupper())} upper letters")
    print(f"{sum(1 for char in text if char.islower())} lower letters")
    print(f"{sum(1 for char in text if char in punct)} punctuation marks")
    print(f"{sum(1 for char in text if char.isspace())} spaces")
    print(f"{sum(1 for char in text if char.isdigit())} digits")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")

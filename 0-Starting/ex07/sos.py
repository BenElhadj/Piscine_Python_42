# sos.py

import sys


def get_morse_code_dict():
    """
    Return a dictionary mapping characters to their Morse code equivalents.

    Returns:
        dict: A dictionary containing Morse code mappings.
    """
    return {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        " ": "/",
    }


def main():
    """
    Convert a string to Morse code.

    Usage:
        python sos.py <string>

    Args:
        <string> (str): A string to convert to Morse code.

    Raises:
        AssertionError: If the arguments are invalid or contain
        unsupported characters.
    """
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")

    morse_code_dict = get_morse_code_dict()
    text = sys.argv[1].upper()
    morse_code = []

    for char in text:
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            raise AssertionError("the arguments are bad")

    print(" ".join(morse_code))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")

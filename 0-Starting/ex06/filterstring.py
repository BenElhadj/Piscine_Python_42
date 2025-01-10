# filterstring.py

import sys
from ft_filter import ft_filter


def main():
    """
    Filter words from a string based on their length.

    Usage:
        python filterstring.py <string> <min_length>

    Args:
        <string> (str): A string containing words.
        <min_length> (int): The minimum length of words to keep.

    Raises:
        AssertionError: If the arguments are invalid.
    """
    args = sys.argv

    if len(args) != 3:
        raise AssertionError("the arguments are bad")

    try:
        S = str(args[1])
        N = int(args[2])
    except ValueError:
        raise AssertionError("the arguments are bad")

    # Split the string into words and filter out non-alphanumeric characters
    words = S.split()
    clean_words = [word for word in words if word.isalnum()]

    # Filter words longer than N using ft_filter and a lambda
    filtered_words = ft_filter(lambda word: len(word) > N, clean_words)

    print(list(filtered_words))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")

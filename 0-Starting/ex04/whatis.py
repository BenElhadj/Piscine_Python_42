# whatis.py

import sys


def main():
    if len(sys.argv) == 1:
        return
    elif len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided")

    try:
        number = int(sys.argv[1])
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        raise AssertionError("argument is not an integer")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")

# format_ft_time.py
import time


def main():

    second = "Seconds since January 1, 1970:"
    current_date = time.time()
    scientific_time = f"{current_date:.2e}"
    notation = "in scientific notation"
    formatted_date = time.strftime("%b %d %Y")

    print(f"{second} {current_date:,.4f} or {scientific_time} {notation}")
    print(formatted_date)


if __name__ == "__main__":
    main()

# Loading.py

import time


def ft_tqdm(lst: range) -> None:  # type: ignore
    """
    A custom progress bar generator similar to tqdm.

    Args:
        lst (range): An iterable to iterate over.

    Yields:
        Any: The next item from the iterable.
    """

    total = len(lst)
    start_time = time.time()

    for i, item in enumerate(lst):
        now = time.time() - start_time
        progress = (i + 1) / total * 100
        if i > 0:
            time_per_item = now / (i + 1)
            remaining_time = time_per_item * (total - (i + 1))
        else:
            remaining_time = 0

        percent = f"{progress:3.0f}%"
        progress_str = f"{'=' * int(progress / 2)}"
        progress_spaces = f"{' ' * (50 - int(progress / 2))}"
        iterations_per_second = (i + 1) / now if now > 0 else 0

        print(
            f"\r{percent}|[{progress_str}>{progress_spaces}]| "
            f"{i + 1}/{total} ["
            f"{time.strftime('%M:%S', time.gmtime(now))}<"
            f"{time.strftime('%M:%S', time.gmtime(remaining_time))}, "
            f"{iterations_per_second:.2f}it/s]",
            end=" ",
        )
        yield item

    print()

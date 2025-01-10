# ft_filter.py


def ft_filter(function, iterable):
    """Return an iterator yielding those items of iterable for which \
function(item)
    is true. If function is None, return the items that are true."""
    return [item for item in iterable if function(item)]

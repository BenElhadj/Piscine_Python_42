# ft_filter.py


def ft_filter(function, iterable):
    return [item for item in iterable if function(item)]

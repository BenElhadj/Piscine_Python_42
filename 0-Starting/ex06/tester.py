from ft_filter import ft_filter

original = filter.__doc__
copy = ft_filter.__doc__

print(copy)  # output: docstring
print(
    "\n______________________copy__________________________\n"
)  # output: copy docstring
print(original)  # output: True
print(
    "\n_____________________original_______________________\n"
)  # output: original docstring
print(original == copy)  # output: True

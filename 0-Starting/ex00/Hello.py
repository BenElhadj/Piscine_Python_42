# Hello.py

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Afficher les structures de données avant la modification
# print(ft_list)
# print(ft_tuple)
# print(ft_set)
# print(ft_dict)

# Modification des chaînes de caractères
ft_list[1] = "World"
ft_tuple = (ft_tuple[0], "France")
ft_set = {"Paris", "Hello"}
ft_dict["Hello"] = "42Paris"

# Afficher les structures de données modifiées
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

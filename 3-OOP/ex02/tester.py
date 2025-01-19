from DiamondTrap import King

Joffrey = King("Joffrey")
print(Joffrey.__dict__)  # {'first_name': 'Joffrey', 'is_alive': True,
# 'family_name': 'Baratheon', '_eyes': 'brown', '_hairs': 'dark'}
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())  # blue
print(Joffrey.get_hairs())  # light
print(Joffrey.__dict__)  # {'first_name': 'Joffrey', 'is_alive': True,
# 'family_name': 'Baratheon', '_eyes': 'blue', '_hairs': 'light'}

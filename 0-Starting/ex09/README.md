# ft_package

## Description

Un package Python simple qui fournit une fonction pour compter les occurrences d'un élément dans une liste.

## Utilisation

```python
from ft_package import count_in_list

lst = ["apple", "banana", "apple"]
print(count_in_list(lst, "apple")) 
```

## Installation

Pour créer le package, exécutez la commande suivante pour générer le package :

```bash
python setup.py sdist bdist_wheel
```

MPour installer le package, installez le package localement avec :

```bash
pip install .
or
pip install ./dist/ft_package-0.0.42.tar.gz
or
pip install dist/ft_package-0.0.42-py3-none-any.whl
```

Pour vérifier l'installation, vérifiez que le package est installé :

```bash
pip list
```

Pour afficher les informations du package :

```bash
pip show -v ft_package
```

Pour tester le package :

```bash
python test_package.py
```

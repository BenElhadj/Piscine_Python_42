# new_student.py

from dataclasses import dataclass, field
import random
import string


def generate_id() -> str:
    """
    Génère un identifiant aléatoire de 15 caractères.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Classe représentant un étudiant.
    """

    name: str
    surname: str
    active: bool = True
    login: str = field(
        init=False
    )  # Ne peut pas être initialisé par l'utilisateur
    id: str = field(
        init=False
    )  # Ne peut pas être initialisé par l'utilisateur

    def __post_init__(self):
        """
        Méthode appelée après l'initialisation de l'objet.
        Génère le login et l'id automatiquement.
        """
        # Génère le login à partir du nom et du prénom
        self.login = (self.name[0] + self.surname).lower()

        # Génère un id aléatoire
        self.id = generate_id()

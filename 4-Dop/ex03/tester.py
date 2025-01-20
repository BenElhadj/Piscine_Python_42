# tester.py

from new_student import Student

# Crée un étudiant avec un nom et un prénom
student = Student(name="Edward", surname="agle")
print(student)

# Essaie de créer un étudiant avec un id personnalisé (doit lever une erreur)
try:
    invalid_student = Student(name="Edvard", surname="agle", id="toto")
except TypeError as e:
    print(e)

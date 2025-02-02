# setup.py

from setuptools import setup  # type: ignore

setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    long_description=open("README.md").read(),
    author="bhamdi",
    author_email="bhamdi@student.42.fr",
    url="https://github.com/BenElhadj/Piscine_Python_42",
    license="42_Paris",
    packages=["ft_package"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: 42_Paris License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
)

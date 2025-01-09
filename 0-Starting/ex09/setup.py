# setup.py

from setuptools import setup

setup(
    name="ft_package",
    version="0.0.42",
    description="A sample test package",
    long_description=open("README.md").read(),
    author="bhamdi",
    author_email="bhamdi@student.42.fr",
    url="https://github.com/BenElhadj/ft_package",
    license="42_Paris",
    packages=["ft_package"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: 42_Paris License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
)
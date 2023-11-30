from setuptools import setup, find_packages

setup(
    name="CPtree",
    version="1.0.0",
    author="Justin Wright",
    description="ACSII Filetree Generator",
    packages=find_packages(),
    install_requires=[
        "typer",
    ],
)

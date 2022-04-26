import setuptools
 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setuptools.setup(
    package_dir={"": "dumbo"},
    packages=["dumbo"],
    long_description=long_description,
    install_requires= [
        "setuptools>=40",
        "wheel",
        "Faker>=13.4.0"
    ]
)
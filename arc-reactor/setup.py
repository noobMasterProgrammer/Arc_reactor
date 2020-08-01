import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='arc-reactor',  
    version='1.0.0',
    author="Abhishek Ghosh",
    author_email="ghoshabhishek1640@gmail.com",
    description="A custom framework for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Abhishek1009/python-projects/tree/master/pyframe",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )
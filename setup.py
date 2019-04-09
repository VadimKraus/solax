import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="solax",
    version="0.0.3",
    author="Robin Wohlers-Reichel",
    author_email="me@robinwr.com",
    description="Solax inverter API client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/squishykid/solax",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

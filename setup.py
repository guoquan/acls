import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="acls",
    version="1.0.0",
    author="guoquan",
    author_email="guoquanscu@gmail.com",
    description="`@cls` - Class Made Aware to Decorator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guoquan/acls",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

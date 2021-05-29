import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="gamuth",
    version="0.0.1",
    description="Guide to Advanced Music Theory",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/fabianmoss/gamuth",
    author="Fabian C. Moss",
    author_email="fabianmoss@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["gamuth"],
    include_package_data=True,
    install_requires=["numpy"],
    entry_points={
        "console_scripts": [
            "gamuth=gamuth.__main__:main",
        ]
    },
)
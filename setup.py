from os import path

from setuptools import find_packages, setup

__author__ = "Arijit Basu"
__email__ = "sayanarijit@gmail.com"
__homepage__ = "https://github.com/sayanarijit/flask-htmldoom"
__description__ = "htmldoom integration for Flask"
__version__ = "v0.1.1"
__license__ = "MIT"
__all__ = [
    "__author__",
    "__email__",
    "__homepage__",
    "__description__",
    "__version__",
    "__license__",
]

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

testing_requires = ["pytest>=4.4.1", "pytest-cov>=2.7.1", "black>=19.3b0"]
dev_requires = testing_requires + ["tox>=3.12.1"]

setup(
    name="Flask-Htmldoom",
    version=__version__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__homepage__,
    author=__author__,
    author_email=__email__,
    license=__license__,
    py_modules=["flask_htmldoom"],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
        "Topic :: Software Development",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    platforms=["Any"],
    keywords="html rendering for flask",
    packages=find_packages(exclude=["contrib", "docs", "tests", "examples"]),
    install_requires=["Flask", "htmldoom>=0.6<0.7"],
    extras_require={"testing": testing_requires, "dev": dev_requires},
    test_suit="pytest",
)

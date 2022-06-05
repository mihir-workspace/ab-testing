from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A python library dedicated for A/B testing analysis'

# Setting up
setup(
    name="ab_testing-analysis",
    version=VERSION,
    author="Mihir Deo",
    author_email="<mihirdeo16@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/mihir-workspace/ab-testing',
    packages={'','ab_testing'},
    install_requires=["pandas","numpy"],
    keywords=['python', 'a/b testing', 'abtest', 'response analysis','conversion rate analysis'],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
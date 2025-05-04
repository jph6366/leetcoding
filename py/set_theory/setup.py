import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="set_theory",
    version="0.1.0",
    url="none",
    license='MIT',

    author="Jackson Hardee",
    author_email="jphardee@gmail.com",

    description="A codebase for informally describing studied aspects of set theory that show up in computer science problems.",
    long_description=read("README.rst"),

    packages=find_packages(exclude=('tests',)),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Engineering :: Data Structures & Algorithms',
    ],
)

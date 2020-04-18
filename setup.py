#!/usr/bin/env python

import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 7, 0):
    raise Exception("This project designed for Python >= 3.7.")

setup(
    name="datapeek",
    version="0.0.2",
    description="Peek at data in a variety of formats",
    author="Andy Herd",
    # author_email="",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        datapeek=datapeek.commands:peek
    """,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)

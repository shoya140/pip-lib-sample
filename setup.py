#!/usr/bin/env python
# coding: utf-8

try:
    from setuptools import setup, find_packages
except ImportError:
    print("Please install setuptools.")

setup(
    name  = 'pip-lib-sample',
    version = '0.1.0',
    description = 'My sample lib.',
    license = 'MIT',
    author = 'Shoya Ishimaru',
    author_email = 'shoya.ishimaru@gmail.com',
    url = 'https://github.com/shoya140/dalmatian',
    packages = find_packages(),
    install_requires = [],
    classifiers = [
      "License :: OSI Approved :: MIT License"
    ]
)
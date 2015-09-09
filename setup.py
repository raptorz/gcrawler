#!/usr/bin/env python

from distutils.core import setup, find_packages

PACKAGE = 'gcrawler'

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

setup(
    name = PACKAGE,
    version = __import__(PACKAGE).__version__,
    description = 'A lightweight crawler framework using gevent.',
    author = 'Raptor Zhang',
    author_email = 'raptor.zh@gmail.com',
    url = 'http://www.github.com/raptorz/gcrawler',
    license = 'BSD',
    platforms = 'any',
    requires = ['gevent'],
    packages = find_packages(),
    zip_safe = Fasle,
)

#!/usr/bin/env python

from distutils.core import setup, find_packages

PACKAGE = 'webget'

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

setup(
    name = PACKAGE,
    version = __import__(PACKAGE).__version__,
    description = 'web UI for wget.',
    author = 'Raptor Zhang',
    author_email = 'raptor.zh@gmail.com',
    url = 'http://www.github.com/raptorz/webget',
    license = 'APL',
    platforms = 'any',
    requires = ['bottle>=0.12', 'mako', 'requests'],
    packages = find_packages(),
    zip_safe = Fasle,
)

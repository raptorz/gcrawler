from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='gcrawler',
      version=version,
      description="A lightweight crawler framework using gevent",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='crawler gevent',
      author='Raptor Zhang',
      author_email='raptor.zh@gmail.com',
      url='https://bitbucket.org/raptorz/gcrawler',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "gevent"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

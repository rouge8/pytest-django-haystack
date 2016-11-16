#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(name='pytest-django-haystack',
      version='0.2.0',
      description='Cleanup your Haystack indexes between tests',
      author='Andy Freeland',
      author_email='andy@andyfreeland.net',
      maintainer='Andy Freeland',
      maintainer_email='andy@andyfreeland.net',
      url='http://github.com/rouge8/pytest-django-haystack',
      py_modules=['pytest_django_haystack'],
      long_description=read('README.rst'),
      install_requires=['pytest>=2.3.4', 'pytest-django>=2.3'],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Testing',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   ],
      # the following makes a plugin available to py.test
      entry_points={'pytest11': ['django_haystack = pytest_django_haystack']})

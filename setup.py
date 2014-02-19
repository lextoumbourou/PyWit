#!/usr/bin/env python
from setuptools import setup


setup(name='PyWit',
      version='0.1.0',
      author='Lex Toumbourou',
      author_email='lextoumbourou@gmail.com',
      description='Python bindings for the Wit HTTP API',
      license='MIT',
      classifiers=[
          'Intended Audience :: Developers',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment'
      ],
      packages=['wit'],
      package_dir={'wit': 'wit'},
      url='https://github.com/lextoumbourou/PyWit',
      install_requires=['requests'])

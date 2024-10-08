#!/usr/bin/env python

import codecs
from setuptools import setup

# Version info -- read without importing
_locals = {}
with open('aiohttp_theme/_version.py') as fp:
    exec(fp.read(), None, _locals)
version = _locals['__version__']

# README into long description
with codecs.open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='aiohttp-theme',
    version=version,
    description='A configurable sidebar-enabled Sphinx theme',
    long_description=readme,
    author='Andrew Svetlov',
    author_email='andrew.svetlov@gmail.com',
    url='https://github.com/aio-libs/aiohttp-theme',
    packages=['aiohttp_theme'],
    include_package_data=True,
    license="BSD License",
    license_files="LICENSE",
    entry_points={
        'sphinx.html_themes': [
            'aiohttp_theme = aiohttp_theme',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)

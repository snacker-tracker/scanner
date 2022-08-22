#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.md').read()
doclink = """
Documentation
-------------

The full documentation is at http://snacker-tracker-scanner.rtfd.org."""

history = open('HISTORY.md').read()

setup(
    name='snacker-tracker-scanner',
    version=os.environ.get('APP_VERSION', "0.1.0-snapshot"),
    description='Pipe barcode scanner input events to a remote web service',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='lmac',
    author_email='leprechaun@gmail.com',
    url='https://github.com/snacker-tracker/scanner',
    packages=[
        'snacker_tracker_scanner',
    ],
    scripts=["scripts/snacker-tracker-scanner"],
    package_dir={'snacker-tracker-scanner': 'snacker_tracker_scanner'},
    include_package_data=True,
    install_requires=["requests"],
    extras_require = {
        "evdev": ["evdev"]
    },
    license='MIT',
    zip_safe=False,
    keywords='barcode scanner snacker-tracker',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)

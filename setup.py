from setuptools import setup
import sys

if sys.version_info < (3,7):
    sys.exit("Python 3.7 required!!!")

setup(
    name='badge',
    version='0.1',
    py_modules=['badge'],
    install_requires=[
        'Click',
        'requests',
        'pillow'
    ],
    entry_points='''
        [console_scripts]
        badge=badge:cli
    ''',
)

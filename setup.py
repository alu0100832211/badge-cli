from setuptools import setup

setup(
    name='badge',
    version='0.1',
    py_modules=['badge'],
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        badge=badge:cli
    ''',
)

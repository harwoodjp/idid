from setuptools import setup

setup(
    name='idid',
    version='0.1',
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        idid=main:main
    ''',
)

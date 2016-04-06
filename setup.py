from setuptools import setup, find_packages

version = '1.0'

REQUIREMENTS = [
    'pyodbc'
]

setup(
    name='pyodbc-database-tools',
    version=version,
    packages=find_packages(),
    url='https://github.com/ziplokk1/database-tools',
    license='LICENSE.txt',
    author='Mark Sanders',
    author_email='sdscdeveloper@gmail.com',
    install_requires=REQUIREMENTS,
    description='Simple context manager for pyodbc database connections.'
)

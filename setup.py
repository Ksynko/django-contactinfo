import os
from setuptools import setup, find_packages

setup(
    name='django-contactinfo',
    version='1.0.0',
    author='Caktus Consulting Group',
    author_email='solutions@caktusgroup.com',
    packages=find_packages(),
    install_requires = [],
    include_package_data = True,
    exclude_package_data={
        '': ['*.sql', '*.pyc', '*.json',],
        'contactinfo': ['media/*',]
    },
    url='http://code.google.com/p/django-contactinfo/',
    license='LICENSE.txt',
    description=\
    'Accept and manage international contact information in Django with ease ',
    long_description=open('README.txt').read(),
)

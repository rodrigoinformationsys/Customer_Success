# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in customer_success/__init__.py
from customer_success import __version__ as version

setup(
	name='customer_success',
	version=version,
	description='cS',
	author='Rodrigo Giacobelli',
	author_email='rodrigogiacobelli@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

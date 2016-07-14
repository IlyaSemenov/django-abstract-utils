from distutils.core import setup
from setuptools import setup, find_packages

"""
Django utils to operate on abstract model classes.
"""

setup(
	name='django-abstract-utils',
	version='0.0.1',
	url='https://github.com/IlyaSemenov/django-abstract-utils',
	license='BSD',
	author='Ilya Semenov',
	author_email='ilya@semenov.co',
	description=__doc__,
	long_description=open('README.rst').read(),
	packages=['django_abstract_utils'],
	install_requires=['Django>=1.8'],
	classifiers=[],
)

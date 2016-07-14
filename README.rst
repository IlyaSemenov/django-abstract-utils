django-abstract-utils
=====================

Currently, this library provides only one method that operates on Django abstract model class:

* ``without`` (or ``AbstractClassWithoutFieldsNamed``) - create a subclass of an abstract Django model class with certain fields **removed**

This was ripped off from someone's Gist. Feel free to submit a PR with authorship!


Installation
============

::

	pip install django_abstract_utils


Usage
=====

.. code:: python

	from django_abstract_utils import without
	from oscar.apps.address.abstract_models import AbstractBillingAddress

	class BillingAddress(without(AbstractBillingAddress, 'phone_number')):
		pass

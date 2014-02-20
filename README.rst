pytest-django-haystack
======================

pytest-django-haystack is a plugin for `pytest <http://pytest.org/>`_ and `pytest-django <http://pytest-django.readthedocs.org/en/latest/>`_ that rebuilds the Haystack index before every test and clears it again after.

Quick start
===========

1. ``pip install pytest-django-haystack``
2. Mark tests with the ``pytest.mark.haystack`` marker.

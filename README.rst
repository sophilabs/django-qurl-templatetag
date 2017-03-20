===============================
Django QUrl Template Tag
===============================


.. image:: https://img.shields.io/pypi/v/django-qurl-templatetag.svg
        :target: https://pypi.python.org/pypi/django-qurl-templatetag

.. image:: https://img.shields.io/travis/sophilabs/django-qurl-templatetag.svg
        :target: https://travis-ci.org/sophilabs/django-qurl-templatetag

.. image:: https://readthedocs.org/projects/django-qurl-templatetag/badge/?version=latest
        :target: http://django-qurl-templatetag.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/sophilabs/django-qurl-templatetag/shield.svg
     :target: https://pyup.io/repos/github/sophilabs/django-qurl-templatetag/
     :alt: Updates

.. image:: https://img.shields.io/codecov/c/github/sophilabs/django-qurl-templatetag.svg
    :target: https://codecov.io/gh/sophilabs/django-qurl-templatetag


A Django template tag to modify url's query string.


Documentation
-------------

The full documentation is at https://django-url-templatetag.readthedocs.org.


Quick Start
-----------

Install Django QUrl Template Tag:

.. code-block::

    pip install django-qurl-templatetag

After installation is done, add ``qurl_templatetag`` to the ``INSTALLED_APPS`` setting in your settings.py file:

.. code-block::

    INSTALLED_APPS = (
        # …
        'qurl_templatetag',
        # …
    )

Tag Usage
---------

.. code-block::

    {% load qurl %}

    {% qurl url [param]* [as <var_name>] %}

    Parameters:
            name=value: replace all values of name by one value
            name=None: remove all values of name
            name+=value: append a new value for name
            name-=value: remove the value of name with the value
            name++: increment the value by one
            name--: decrement the value by one

    Example:

        {% qurl '/search?page=1&color=blue&color=green' order='name' page=None color+='red' color-='green' %}
        Output: /search?color=blue&order=name&color=red

        {% qurl request.get_full_path order='name' %}


Library Usage
-------------

A Qurl object has a set of chainable methods to modify the querystring parameters.

Available methods are:

* set: replace all values of name by one value, parameter is removed when value is None
* add: append a new value for name
* remove: remove the value of name with the value
* inc: increment the value by another value (optional, defaults to 1)
* dec: decrement the value by another value (optional, defaults to 1)
* get: build the url

.. code-block::

    from qurl_templatetag import Qurl

    >>> Qurl('http://www.sophilabs.co/?page=1&tags=python')\
            .inc('page', value=2)\
            .add('tags', 'django')\
            .add('tags', 'web')\
            .remove('tags', 'python')\
            .get()
    http://www.sophilabs.co/?page=3&tags=django&tags=web


Tests
-----

.. code-block::

    $ pip install -r requirements/test.pip
    $ python runtests.py

About
-----

.. image:: https://s3.amazonaws.com/sophilabs-assets/logo/logo_300x66.gif
    :target: https://sophilabs.co

Django Qurl Template Tag is maintained and funded by sophilabs, inc. The names and logos for
sophilabs are trademarks of sophilabs, inc.

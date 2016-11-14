===============================
Django QUrl Template Tag
===============================


.. image:: https://img.shields.io/pypi/v/django-qurl-templatetag.svg
        :target: https://pypi.python.org/pypi/django-qurl-templatetag

.. image:: https://img.shields.io/travis/sophilabs/django-qurl-templatetag.svg
        :target: https://travis-ci.org/sophilabs/django-qurl-templatetag

.. image:: https://readthedocs.org/projects/django-qurl-templatetag/badge/?version=latest
        :target: https://django-qurl-templatetag.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/sophilabs/django-qurl-templatetag/shield.svg
     :target: https://pyup.io/repos/github/sophilabs/django-qurl-templatetag/
     :alt: Updates

A Django template tag to modify url's query string.


Installation
------------
.. code-block::

    pip install -e git+https://github.com/sophilabs/django-qurl-templatetag.git#egg=django-qurl-templatetag

After installation is done, add ``qurl_templatetag`` to the ``INSTALLED_APPS`` setting in your settings.py file:

.. code-block::

    INSTALLED_APPS = (
        # …
        'qurl_templatetag',
    )



Usage
-----

Append, remove or replace query string parameters from an url (preserve order)

.. code-block::

    {% load qurl %}

    {% qurl url [param]* [as <var_name>] %}

    Parameters:
            name=value: replace all values of name by one value
            name=None: remove all values of name
            name+=value: append a new value for name
            name-=value: remove the value of name with the value

    Example:

        {% qurl '/search?page=1&color=blue&color=green' order='name' page=None color+='red' color-='green' %}
        Output: /search?color=blue&order=name&color=red

        {% qurl request.get_full_path order='name' %}

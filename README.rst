django-qurl-templatetag
-----------------------

Append, remove or replace query string parameters from an url (preserve order)

.. image:: https://travis-ci.org/sophilabs/django-qurl-templatetag.png?branch=master


Installation
============
.. code-block::

    pip install django-qurl-templatetag

After installation is done, add ``qurltemplatetag`` to the ``INSTALLED_APPS`` setting in your settings.py file:

.. code-block::

    INSTALLED_APPS = (
        # …
        'qurltemplatetag',
    )



Usage
=====

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

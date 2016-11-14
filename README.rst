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

Usage
-----

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


Tests
-----

.. code-block::

    $ pip install -r requirements/test.pip
    $ python runtests.py

About
-----

.. image:: https://res.cloudinary.com/jsconfuy/image/upload/c_pad,f_auto,h_200,w_200,e_trim/v1426608244/xuwbunompvfjaxuazlwo.png
    :target: https://sophilabs.co

Django Qurl Template Tag is maintained and funded by sophilabs, inc. The names and logos for
sophilabs are trademarks of sophilabs, inc.

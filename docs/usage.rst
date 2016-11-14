=====
Usage
=====

After installation is done, add ``qurl_templatetag`` to the ``INSTALLED_APPS`` setting in your settings.py file:

.. code-block::

    INSTALLED_APPS = (
        # …
        'qurl_templatetag',
        # …
    )


Then just load the template tag into your template file and use it.

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

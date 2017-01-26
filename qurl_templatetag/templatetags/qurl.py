"""
qurl is a tag to append, remove or replace query string
parameters from an url (preserve order)
"""

import re
import django

from django.utils.encoding import smart_str
from django.template import Library, Node, TemplateSyntaxError
from django.utils import six

if six.PY3:
    from urllib.parse import urlparse, parse_qsl, urlunparse, urlencode
else:
    from urlparse import urlparse, parse_qsl, urlunparse
    from urllib import urlencode


register = Library()


@register.tag
def qurl(parser, token):
    """
    Append, remove or replace query string parameters (preserve order)

        {% qurl url [param]* [as <var_name>] %}

    param:
            name=value: replace all values of name by one value
            name=None: remove all values of name
            name+=value: append a new value for name
            name-=value: remove the value of name with the value
            name++: increment value by one
            name--: decrement value by one

    Example::

        {% qurl '/search?page=1&color=blue&color=green'
                 order='name' page=None color+='red' color-='green' %}
        Output: /search?color=blue&order=name&color=red

        {% qurl request.get_full_path order='name' %}
    """
    bits = token.split_contents()
    if len(bits) < 2:
        raise TemplateSyntaxError(
            '"{0}" takes at least one argument (url)'.format(bits[0]))

    url = parser.compile_filter(bits[1])

    asvar = None
    bits = bits[2:]
    if len(bits) >= 2 and bits[-2] == 'as':
        asvar = bits[-1]
        bits = bits[:-2]

    qs = []
    if len(bits):
        kwarg_re = re.compile(r'(\w+)(\-=|\+=|=|\+\+|\-\-)(.*)')
        for bit in bits:
            match = kwarg_re.match(bit)
            if not match:
                raise TemplateSyntaxError('Malformed arguments to url tag')
            name, op, value = match.groups()
            qs.append((name, op, parser.compile_filter(value),))

    return QURLNode(url, qs, asvar)


class Qurl(object):

    def __init__(self, url):
        self.url = url
        self._qsl = parse_qsl(urlparse(url).query)

    def set(self, name, value):
        clone = self._clone()
        if django.VERSION[0] <= 1 and django.VERSION[1] <= 4:
            value = value or None
        clone._qsl = [(q, v) for (q, v) in self._qsl if q != name]
        if value is not None:
            clone._qsl.append((name, value))
        return clone

    def add(self, name, value):
        clone = self._clone()
        clone._qsl = [p for p in self._qsl
                      if not(p[0] == name and p[1] == value)]
        clone._qsl.append((name, value,))
        return clone

    def remove(self, name, value):
        clone = self._clone()
        clone._qsl = [qb for qb in self._qsl if qb != (name, str(value))]
        return clone

    def inc(self, name, value=1):
        clone = self._clone()
        clone._qsl = [(q, v) if q != name else (q, int(v) + value)
                      for (q, v) in self._qsl]
        if name not in dict(clone._qsl).keys():
            clone._qsl.append((name, value))
        return clone

    def dec(self, name, value=1):
        return self._clone().inc(name, -value)

    def _clone(self):
        return Qurl(self.get())

    def get(self):
        parsed = list(urlparse(self.url))
        parsed[4] = urlencode(self._qsl)
        return urlunparse(parsed)


@register.tag
def rqurl(parser, token):
    return qurl(parser, token, True)


class QURLNode(Node):
    """Implements the actions of the qurl tag."""

    def __init__(self, url, qs, asvar):
        self.url = url
        self.qs = qs
        self.asvar = asvar

    def render(self, context):
        render_qurl = Qurl(self.url.resolve(context))

        for name, op, value in self.qs:
            name = smart_str(name)
            value = value.resolve(context)
            value = smart_str(value) if value is not None else None
            if op == '+=':
                render_qurl = render_qurl.add(name, value)
            elif op == '-=':
                render_qurl = render_qurl.remove(name, value)
            elif op == '=':
                render_qurl = render_qurl.set(name, value)
            elif op == '++':
                render_qurl = render_qurl.inc(name)
            elif op == '--':
                render_qurl = render_qurl.dec(name)

        url = render_qurl.get()
        if self.asvar:
            context[self.asvar] = url
            return ''
        else:
            return url

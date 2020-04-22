import django
from urllib.parse import urlparse, parse_qsl, urlunparse, urlencode


class Qurl(object):
    """
    Initialized with a url, provides a few chainable methods
    to manipulate its querystring.
    eg:
        >>> Qurl('http://www.sophilabs.co/?page=1&tags=python')\
                .inc('page')\
                .add('tags', 'django')\
                .add('tags', 'web')\
                .remove('tags', 'python')\
                .get()
        http://www.sophilabs.co/?page=2&tags=django&tags=web
    """

    def __init__(self, url):
        self.url = url
        self._qsl = parse_qsl(urlparse(url).query)

    def set(self, name, value):
        """ Assign a value, remove if it's None """
        clone = self._clone()
        if django.VERSION[0] <= 1 and django.VERSION[1] <= 4:
            value = value or None
        clone._qsl = [(q, v) for (q, v) in self._qsl if q != name]
        if value is not None:
            clone._qsl.append((name, value))
        return clone

    def add(self, name, value):
        """ Append a value to multiple value parameter. """
        clone = self._clone()
        clone._qsl = [p for p in self._qsl
                      if not(p[0] == name and p[1] == value)]
        clone._qsl.append((name, value,))
        return clone

    def remove(self, name, value):
        """ Remove a value from multiple value parameter. """
        clone = self._clone()
        clone._qsl = [qb for qb in self._qsl if qb != (name, str(value))]
        return clone

    def inc(self, name, value=1):
        """ Increment value """
        clone = self._clone()
        clone._qsl = [(q, v) if q != name else (q, int(v) + value)
                      for (q, v) in self._qsl]
        if name not in dict(clone._qsl).keys():
            clone._qsl.append((name, value))
        return clone

    def dec(self, name, value=1):
        """ Decrement value """
        return self._clone().inc(name, -value)

    def _clone(self):
        return Qurl(self.get())

    def get(self):
        parsed = list(urlparse(self.url))
        parsed[4] = urlencode(self._qsl)
        return urlunparse(parsed)

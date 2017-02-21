#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_qurl_templatetag
----------------------------------

Tests for `qurl_templatetag` module.
"""


from django.test import TestCase
from django.template import Template, Context, TemplateSyntaxError
from qurl_templatetag.templatetags.qurl import Qurl


class QUrlTemplateTagTestCase(TestCase):

    def test_qurl_append(self):
        out = Template(
            '{% load qurl %}'
            '{% qurl "http://sophilabs.com/?a=1" a+="2" a-="1" %}'
        ).render(Context())
        self.assertEqual(out, 'http://sophilabs.com/?a=2')

    def test_qurl_set(self):
        out = Template(
            '{% load qurl %}'
            '{% qurl "http://sophilabs.com/?a=1" a=None b="1" %}'
        ).render(Context())
        self.assertEqual(out, 'http://sophilabs.com/?b=1')

    def test_qurl_as(self):
        context = Context()
        Template(
            '{% load qurl %}'
            '{% qurl "http://sophilabs.com/?a=1" a=None as url %}'
        ).render(context)
        self.assertEqual(context.get('url'), 'http://sophilabs.com/')

    def test_qurl_inc(self):
        out = Template(
            '{% load qurl %}'
            '{% qurl "http://sophilabs.com/?a=1" a++ %}'
        ).render(Context())
        self.assertEqual(out, 'http://sophilabs.com/?a=2')

        out = Template(
            '{% load qurl %}'
            '{% qurl "http://sophilabs.com/?a=1" b++ %}'
        ).render(Context())
        self.assertEqual(out, 'http://sophilabs.com/?a=1&b=1')

    def test_qurl_dec(self):
        out = Template(
            '{% load qurl %}'
            '{% qurl "http://sophilabs.com/?a=1" a-- %}'
        ).render(Context())
        self.assertEqual(out, 'http://sophilabs.com/?a=0')

        out = Template(
            '{% load qurl %}'
            '{% qurl "http://sophilabs.com/?a=1" b-- %}'
        ).render(Context())
        self.assertEqual(out, 'http://sophilabs.com/?a=1&b=-1')

    def test_malformed(self):
        template = """
            {% load qurl %}
            {% qurl "http://sophilabs.com/?a=1" a**2 %}
        """
        self.assertRaises(TemplateSyntaxError, Template, template)


class QurlTestCase(TestCase):

    def test_set(self):
        qurl = Qurl('http://sophilabs.com/?a=1')

        qurl = qurl.set('a', 2)
        self.assertEqual(qurl.get(), 'http://sophilabs.com/?a=2')

        qurl = qurl.set('b', 1)
        self.assertEqual(qurl.get(), 'http://sophilabs.com/?a=2&b=1')

        qurl = qurl.set('a', 3)
        self.assertEqual(qurl.get(), 'http://sophilabs.com/?b=1&a=3')

    def test_add(self):
        qurl = Qurl('http://sophilabs.com/?a=1')

        qurl = qurl.add('a', 2)
        self.assertEqual(qurl.get(), 'http://sophilabs.com/?a=1&a=2')

        qurl = qurl.add('b', 9)
        self.assertEqual(qurl.get(), 'http://sophilabs.com/?a=1&a=2&b=9')

    def test_remove(self):
        qurl = Qurl('http://sophilabs.com/?a=1&a=3')

        qurl = qurl.remove('a', 3)
        self.assertEqual(qurl.get(), 'http://sophilabs.com/?a=1')

    def test_inc(self):
        qurl = Qurl('http://sophilabs.com/?a=1')

        qurl = qurl.inc('a', 1)
        self.assertEqual(qurl.get(), 'http://sophilabs.com/?a=2')

        qurl = qurl.inc('b', 1)
        self.assertEqual(qurl.get(), 'http://sophilabs.com/?a=2&b=1')

    def test_dec(self):
        qurl = Qurl('http://sophilabs.com/?a=4')

        qurl = qurl.dec('a', 1)
        self.assertEqual(qurl.get(), 'http://sophilabs.com/?a=3')

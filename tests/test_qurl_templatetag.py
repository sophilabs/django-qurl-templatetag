#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_qurl_templatetag
----------------------------------

Tests for `qurl_templatetag` module.
"""


from django.test import TestCase
from django.template import Template, Context


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

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

version = '0.0.14'

setup(
    name='django-qurl-templatetag',
    version=version,
    description="A Django template tag to modify url's query string.",
    long_description=readme,
    author='Sophilabs',
    author_email='hi@sophilabs.com',
    url='https://github.com/sophilabs/django-qurl-templatetag',
    packages=[
        'qurl_templatetag', 'qurl_templatetag.templatetags'
    ],
    package_dir={
        'qurl_templatetag': 'qurl_templatetag'
    },
    include_package_data=True,
    install_requires=requirements,
    license='MIT license',
    zip_safe=False,
    keywords='django, templatetag',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

from distutils.core import setup


setup(name='django-qurl-templatetag',
      version='0.0.1',
      packages=['qurltemplatetag', 'qurltemplatetag.templatetags'],
      license='MIT',
      author='Sophilabs',
      author_email='hi@sophilabs.com',
      url='https://github.com/sophilabs/django-qurl-templatetag/',
      description='qurl is a tag to append, remove or replace query '
                  'string parameters from an url (preserve order)')

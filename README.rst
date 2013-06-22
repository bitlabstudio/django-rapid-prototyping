Django Rapid Prototyping
============

A reusable Django app that helps to create prototypes and cost estimations.

Installation
------------

To get the latest stable release from PyPi::

    $ pip install django-rapid-prototyping

To get the latest commit from GitHub::

    $ pip install -e git+git://github.com/bitmazk/django-rapid-prototyping.git#egg=rapid_prototyping

TODO: Describe further installation steps (edit / remove the examples below):

Add ``rapid_prototyping`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'rapid_prototyping',
    )

Add the ``rapid_prototyping`` URLs to your ``urls.py``::

    urlpatterns = patterns('',
        ...
        url(r'^VAR_URL_HOOK/', include('rapid_prototyping.urls')),
    )

Don't forget to migrate your database::

    ./manage.py migrate rapid_prototyping


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-rapid-prototyping
    $ python setup.py install
    $ pip install -r dev_requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch

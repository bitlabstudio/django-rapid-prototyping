Django Rapid Prototyping
========================

A reusable Django app that helps to create prototypes and cost estimations.

Installation
------------

To get the latest stable release from PyPi::

    $ pip install django-rapid-prototyping

To get the latest commit from GitHub::

    $ pip install -e git+git://github.com/bitmazk/django-rapid-prototyping.git#egg=rapid_prototyping

Add ``rapid_prototyping`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'rapid_prototyping',
    )

Add the ``RapidPrototypingView`` from ``django-libs`` to your ``urls.py``::

    from django_libs.views import RapidPrototypingView

    urlpatterns = patterns('',
        ...
        url(r'^p/(?P<template_path>.*)$',
            RapidPrototypingView.as_view(),
            name='prototype'),
    )

We had that view in django-libs long before we started this app. In the
future we might deprecate that view in django-libs and move it over here.


Usage
-----

In your ``base.html`` add the following block to the bottom of your site::

    {% block costs_footer_container %}
    <div class="costsFooter">
        <div class="container">
            <div class="row">
                <div class="span12">
                    {% block costs_footer %}{% endblock %}
                </div>
            </div>
        </div>
    </div>
    {% endblock %}

    {% comment %}
    Include this sctipt after your jQuery include.
    {% endcomment %}
    <script src="{{ STATIC_URL }}proto/js/calculate_total.js"></script>

Now create an ``index.html`` like so::

    {% extends "base.html" %}
    {% load libs_tags proto_tags %}

    {% block main %}
    <h1>Project Prototype</h1>
    <ul>
        <li><a href="/p/home.html">Landing Page</a></li>
        {% comment %}Add links to all pages that are part of your prototype here{% endcomment %}
    </ul>
    {% endblock %}

    {% block costs_footer %}
    <table class="table table-bordered table-hover">
        {% include "proto/costs_table_head.html" %}
        <tbody>
            {% load_context "yourproject.context.home_costs" %}
            {% include "proto/costs_table_body.html" %}
            {% comment %}
                Load context and include table body for all pages that are part of your prototype here
                {% load_context "yourproject.context.search_results_costs" %}
                {% include "proto/costs_table_body.html" %}
            {% endcomment %}
            {% include "proto/costs_total.html" %}
        </tbody>
    </table>
    {% endblock %}

For each page that you create, you need to create a context file which defines
the estimated costs for all subtasks that need to be done in order to get that
page up and running. Such a file could look like this::

    # in yourproject/context/home_costs.py
    from rapid_prototyping.context.utils import append_overhead_costs, get_counter
    HOURLY_RATE = 70
    MAIN_ID = 100
    counter = [-1]
    costs = [
        {
            'id': MAIN_ID + get_counter(counter)[0],
            'task': 'Create logo',
            'time': 240,
        },
        {
            'id': MAIN_ID + get_counter(counter)[0],
            'task': 'Create color scheme',
            'time': 120,
        },
        {
            'id': MAIN_ID + get_counter(counter)[0],
            'task': 'Create email form',
            'time': 30,
        }
    ]
    costs = append_overhead_costs(costs, MAIN_ID + get_counter(counter)[0])

When you have done all this you should be able to visit ``/p/home.html`` and
see your template with a table of costs below. You should also be able to see
``/p/index.html`` with a list of all pages and a table of total project costs.


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

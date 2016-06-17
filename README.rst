Django Rapid Prototyping
========================

A reusable Django app that helps to create prototypes and cost estimations.

Installation
------------

To get the latest stable release from PyPi::

    $ pip install django-rapid-prototyping

To get the latest commit from GitHub::

    $ pip install -e git+git://github.com/bitmazk/django-rapid-prototyping.git#egg=rapid_prototyping

Add ``django_libs`` and ``rapid_prototyping`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'django_libs'
        'rapid_prototyping',
    )

Add the ``RapidPrototypingView`` from ``django-libs`` and include the
``urls.py`` of this app in your main ``urls.py``::

    from django_libs.views import RapidPrototypingView

    urlpatterns = [
        url(r'^p/', include('rapid_prototyping.urls')),
        url(r'^p/(?P<template_path>.*)$',
            RapidPrototypingView.as_view(),
            name='prototype'),
    ]

Add the mandatory settings to your ``settings.py``. See heading ``Settings``
below.

Settings
--------

RAPID_PROTOTYPING_SPRINTS_MODULE
++++++++++++++++++++++++++++++++

Mandatory setting. Should be a fully qualified name to the ``sprints``
array in your ``sprints`` module somewhere in your project. This would usually
be something like ``myproject.context.sprints.sprints``.

Of course you have to create that file and add the ``sprints`` array. See
heading ``Sprints`` below.


RAPID_PROTOTYPING_HOURLY_RATE
+++++++++++++++++++++++++++++

Mandatory setting. Set this to an integer representing your hourly rate.


Usage
-----

In your ``proto/p_base.html`` add the following block to the bottom of your site::

    {% block costs_footer_container %}
    <div class="costsFooter">
        <div class="container">
            <div class="row">
                <div class="col-sm-12">
                    {% block costs_footer %}{% endblock %}
                </div>
            </div>
        </div>
    </div>
    {% endblock %}

    {% comment %}Include this sctipt after your jQuery include.{% endcomment %}
    <script src="{% static "rapid_prototyping/js/calculate_total.js" %}"></script>

Now create a ``p_index.html`` like so::

    {% extends "proto/p_base.html" %}
    {% load libs_tags rapid_prototyping_tags %}

    {% block main %}
    <h1>Project Prototype</h1>
    <ul>
        <li><a href="/p/home.html">Landing Page</a></li>
        {% comment %}Add links to all pages that are part of your prototype here{% endcomment %}
    </ul>
    {% endblock %}

    {% block costs_footer %}
    <table class="table table-bordered table-hover">
        {% include "rapid_prototyping/costs_table_head.html" %}
        <tbody>
            {% load_context "yourproject.context.home_costs" %}
            {% include "rapid_prototyping/costs_table_body.html" %}
            {% comment %}
                Load context and include table body for all pages that are part of your prototype here
                {% load_context "yourproject.context.search_results_costs" %}
                {% include "rapid_prototyping/costs_table_body.html" %}
            {% endcomment %}
            {% include "rapid_prototyping/costs_total.html" %}
        </tbody>
    </table>
    {% endblock %}

For each page that you create, you need to create a context file which defines
the estimated costs for all subtasks that need to be done in order to get that
page up and running. Such a file could look like this::

    # in yourproject/context/home_costs.py
    from rapid_prototyping.context.utils import append_overhead_costs, get_counter

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

When you have done all this you should be able to visit
``/p/proto/p_home.html`` and see your template with a table of costs below. You
should also be able to see ``/p/p_index.html`` with a list of all pages and a
table of total project costs.

Sprints
-------

If you have done all the above, you will have some prototype pages with tables
at the bottom that show planned tasks for each page. You will also have an
index page which shows all tasks for the whole project.

Now you migiht want to group tasks into sprints and track the actual time that
has been taken to implement a certain task.

First of all, create a ``yourproject/context/sprints.py`` like so::

    sprints = [
        {
            'id': 1,
            'title': 'Week 32',
        },
        {
            'id': 2,
            'title': 'Week 33',
        },
    ]

That's all. It's just an array of dicts, each dict describes a sprint. The
title can be useful when rendering the list of sprints, the important part
is the ``id``.

In order to assign tasks to a sprint, open the corresponding ``*_costs.py``
file and add some more information to the task's dict::

    costs = [
        {
            'id': MAIN_ID + get_counter(counter)[0],
            'task': 'Create logo',
            'time': 240,
            'developer_time': 300,
            'actual_time': 450,
            'link': 'http://www.trello.com/',
            'sprint': 1,
        },
    ...

The additional columns are the following:

**developer_time**: While ``time`` is the time the project manager estimated
at the very beginning when communicating with the customer, ``developer_time``
is the time that the person who actually implementes this estimates at the
beginning of a sprint. This can be different from ``time`` because as the
project progresses and patterns / frameworks emerge, some tasks can become
much easier or much more difficult than initally planned.

**actual_time**: This is the time that the developer actually took in order
to complete the task.

**link**: If you are using some other software, like www.trello.com to manage
your project, you can add a link to the corresponding ticket for this task
in your other software here.

**sprint**: This must be one of the IDs that you have defined in your
``sprints.py``.

If you have done all the above, you should be able to visit ``/p/sprints/``.

You will now see your sprints with their assigned tasks. Before you start a
sprint, you might want to note down the total edeveloper estimated time at
the beginning of the sprint. This is useful because if you can't finish
some of the tasks and move them into the next sprint, the total will change
and you will not know, how much time you initially estimated.

Add the total developer estimated time like so::

    sprints = [
        {
            'id': 1,
            'title': 'Week 32',
            'estimated_time': 1350,
        },
        {
            'id': 2,
            'title': 'Week 33',
        },
    ]

After your sprint, you might want to note down which tasks could not be
completed and how much time had been estimated for these tasks::

    sprints = [
        {
            'id': 1,
            'title': 'Week 32',
            'estimated_time': 1350,
            'unfinished_tasks': [300, 403, 407, 502, 503, 510],
            'unfinished_time': 360,
        },
        {
            'id': 2,
            'title': 'Week 33',
        },
    ]

At this point you must be careful to never add a new task in front of another
task because then all IDs would be incremented and the IDs you noted down here
would no longer be correct.


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

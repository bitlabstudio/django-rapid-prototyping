"""Templatetags for the rapid_prototyping app."""
from django import template
from django.conf import settings


register = template.Library()


@register.filter
def calculate_costs(minutes, hourly_rate):
    """
    Returns the costs for a task based on time and hourly rate.

    Usage::

        {{ item.time|calculate_costs:HOURLY_RATE }}

    """
    return round(float(minutes) / 60 * hourly_rate, 2)


@register.simple_tag
def get_difference(time, actual_time):
    """
    Returns the difference in percent for two given times.

    If it returns 1 it means that the task was finished as planned.
    If it returns n > 1 it means that the task took n% longer than planned
    If it returns n < 1 it means that the task took n% lesser than planned

    """
    return round(float(actual_time) / float(time), 2)


@register.assignment_tag
def get_hourly_rate(item_rate):
    """
    Returns the item rate if given, otherwise the default rate.

    Usage::

        {% get_hourly_rate item.rate as hourly_rate %}
        {{ hourly_rate %}

    """
    if item_rate is None or item_rate is '':
        return settings.RAPID_PROTOTYPING_HOURLY_RATE
    return item_rate

"""Templatetags for the rapid_prototyping app."""
from django import template


register = template.Library()


@register.filter
def calculate_costs(minutes, hourly_rate):
    """
    Returns the costs for a task based on time and hourly rate.

    Usage::

        {{ item.time|calculate_costs:HOURLY_RATE }}

    """
    return float(minutes) / 60 * hourly_rate


@register.assignment_tag
def get_hourly_rate(item_rate, default_rate):
    """
    Returns the item rate if given, otherwise the default rate.

    Usage::

        {% get_hourly_rate item.rate HOURLY_RATE as hourly_rate %}
        {{ hourly_rate %}

    """
    return item_rate is None and default_rate or item_rate

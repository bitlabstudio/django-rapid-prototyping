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

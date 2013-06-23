"""Tests for the templatetags of the rapid_prototyping app."""
from django.test import TestCase

from ..templatetags.rapid_prototyping_tags import (
    calculate_costs,
    get_hourly_rate,
)


class CalculateCostTestCase(TestCase):
    """Tests for the ``calculate_costs`` template filter."""
    longMessage = True

    def test_tag(self):
        result = calculate_costs(30, 70)
        self.assertEqual(result, float(30) / 60 * 70, msg=(
            'Tag should assume that the first parameter represents minutes'
            ' and the second parameter represents an hourly rate. It should'
            ' Correctly calculate the costs for the task based on the minutes'
            ' and the rate.'))


class GetHourlyRateTestCase(TestCase):
    """Tests for the ``get_hourly_rate`` assignment tag."""
    longMessage = True

    def test_tag(self):
        result = get_hourly_rate(None, 70)
        self.assertEqual(result, 70, msg=(
            'If not item rate has been given, the default hourly rate should'
            ' be returned'))

        result = get_hourly_rate(50, 70)
        self.assertEqual(result, 50, msg=(
            'If an item rate is given, it should override the default hourly'
            ' rate and be returned.'))

        result = get_hourly_rate(0, 70)
        self.assertEqual(result, 0, msg=(
            'If the item rate is given and it is 0, it should return 0. This'
            ' is to enable defining tasks that are given away for free.'))

"""Tests for the templatetags of the rapid_prototyping app."""
from django.test import TestCase

from ..templatetags.rapid_prototyping_tags import (
    calculate_costs,
    get_difference,
    get_hourly_rate,
)


class CalculateCostTestCase(TestCase):
    """Tests for the ``calculate_costs`` template filter."""
    longMessage = True

    def test_tag(self):
        result = calculate_costs(380, 70)
        self.assertEqual(result, round(float(380) / 60 * 70, 2), msg=(
            'Tag should assume that the first parameter represents minutes'
            ' and the second parameter represents an hourly rate. It should'
            ' Correctly calculate the costs for the task based on the minutes'
            ' and the rate.'))


class GetDifferenceTestCase(TestCase):
    """Tests for the ``get_difference`` simple tag."""
    longMessage = True

    def test_tag(self):
        result = get_difference(100, 100)
        self.assertEqual(result, 1, msg=(
            'If there is no difference, it should return 1'))
        result = get_difference(100, 50)
        self.assertEqual(result, 0.5, msg=(
            'If actual time was less than estimated time, it should return'
            ' something less than 1'))
        result = get_difference(100, 150)
        self.assertEqual(result, 1.5, msg=(
            'If actual time was more than estimated time, it should return'
            ' something bigger than 1'))


class GetHourlyRateTestCase(TestCase):
    """Tests for the ``get_hourly_rate`` assignment tag."""
    longMessage = True

    def test_tag(self):
        result = get_hourly_rate(None)
        self.assertEqual(result, 70, msg=(
            'If not item rate has been given, the default hourly rate should'
            ' be returned'))

        result = get_hourly_rate(50)
        self.assertEqual(result, 50, msg=(
            'If an item rate is given, it should override the default hourly'
            ' rate and be returned.'))

        result = get_hourly_rate(0)
        self.assertEqual(result, 0, msg=(
            'If the item rate is given and it is 0, it should return 0. This'
            ' is to enable defining tasks that are given away for free.'))

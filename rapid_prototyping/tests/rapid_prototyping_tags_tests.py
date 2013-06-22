"""Tests for the templatetags of the rapid_prototyping app."""
from django.test import TestCase

from ..templatetags.rapid_prototyping_tags import calculate_costs


class CalculateCostTestCase(TestCase):
    """Tests for the ``calculate_costs`` templatetag."""
    longMessage = True

    def test_tag(self):
        result = calculate_costs(30, 70)
        self.assertEqual(result, float(30) / 60 * 70, msg=(
            'Tag should assume that the first parameter represents minutes'
            ' and the second parameter represents an hourly rate. It should'
            ' Correctly calculate the costs for the task based on the minutes'
            ' and the rate.'))

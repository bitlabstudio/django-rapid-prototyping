"""Tests for the context utility functions."""
from django.test import TestCase

from ..context.utils import append_overhead_costs, get_counter, get_sprints


class AppendOverheadCostsTestCase(TestCase):
    """Tests for the ``append_overhead_costs`` function."""
    longMessage = True

    def test_function(self):
        costs = [
            {
                'id': 1,
                'task': 'Test',
                'time': 60,
            },
            {
                'id': 2,
                'task': 'Test2',
                'time': 60,
            },
        ]
        costs = append_overhead_costs(costs, 3)
        self.assertEqual(len(costs), 3, msg=(
            'The function should add a new item to the list.'))
        self.assertEqual(costs[2]['time'], 120 * 0.15, msg=(
            'The function should add 15% to the total costs.'))


class GetCounterTestCase(TestCase):
    """Tests for the ``get_counter`` function."""
    longMessage = True

    def test_function(self):
        counter = [-1]
        get_counter(counter)
        self.assertEqual(counter[0], 0, msg=(
            'The function should change the list and increase the value by'
            ' one.'))


class GetSprintsTestCase(TestCase):
    """Tests for the ``get_sprints`` function."""
    longMessage = True

    def test_function(self):
        result = get_sprints()
        self.assertEqual(result[0]['id'], 1, msg=(
            'Should return the first sprint as set up in the test_app'))
        self.assertEqual(result[0]['tasks'][0]['id'], 100, msg=(
            'Should add the tasks that belong to this sprint'))

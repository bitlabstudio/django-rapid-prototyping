"""Tests for the views of the rapid_prototyping app."""
from django.test import TestCase

from django_libs.tests.mixins import ViewRequestFactoryTestMixin

from ..views import SprintListView


class SprintListViewTestCase(ViewRequestFactoryTestMixin, TestCase):
    """Tests for the ``SprintListView`` class based view."""
    view_class = SprintListView

    def test_view(self):
        resp = self.is_callable()
        self.assertTrue('sprints' in resp.context_data, msg=(
            'Sprints have been added to the context data'))

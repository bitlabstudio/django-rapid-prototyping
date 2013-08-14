"""Tests for the views of the rapid_prototyping app."""
from mock import patch

from django.test import TestCase, RequestFactory

from ..views import SprintListView


class SprintListViewTestCase(TestCase):
    """Tests for the ``SprintListView`` class based view."""
    longMessage = True

    @patch('rapid_prototyping.views.get_sprints')
    def test_view(self, get_sprints_mock):
        req = RequestFactory().get('/')
        view = SprintListView()
        resp = view.dispatch(req)
        self.assertEqual(resp.status_code, 200, msg=(
            'View is callable'))
        self.assertTrue('sprints' in resp.context_data, msg=(
            'Sprints have been added to the context data'))

"""URLs for the rapid_prototyping app."""
from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^sprints/$',
        views.SprintListView.as_view(),
        name='rapid_prototyping_sprint_list'),
)

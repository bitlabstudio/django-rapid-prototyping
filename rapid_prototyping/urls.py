"""URLs for the rapid_prototyping app."""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^sprints/$',
        views.SprintListView.as_view(),
        name='rapid_prototyping_sprint_list'),
]

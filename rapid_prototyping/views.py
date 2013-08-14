"""Views for the rapid_prototyping app."""
from django.views.generic import TemplateView

from .context.utils import get_sprints


class SprintListView(TemplateView):
    template_name = 'rapid_prototyping/sprints.html'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super(SprintListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(SprintListView, self).get_context_data(**kwargs)
        sprints = get_sprints()
        ctx.update({
            'sprints': sprints,
        })
        return ctx

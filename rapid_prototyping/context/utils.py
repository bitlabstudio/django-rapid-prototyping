"""Utility functions that are useful for template context modules."""
from operator import itemgetter
import pkgutil

from django.conf import settings

from django_libs.loaders import load_member_from_setting, load_member


def get_sprints():
    """
    Returns all sprints, enriched with their assigned tasks.

    The project should only have one ``sprints.py`` module. We will define it's
    path via the ``RAPID_PROTOTYPING_SPRINTS_MODULE`` setting. The setting
    should be the fully qualified name of the ``sprints.py`` module (i.e.
    ``projectname.context.sprints.sprints``).

    Furthermore the project can have any amount of ``*_costs.py`` modules in
    any folder (as long as they are on the pythonpath).

    This function will find all ``*_costs.py`` modules and add those tasks,
    that have been assigned to a sprint, to the corresponding sprints in the
    ``sprints.py`` module.

    """
    sprints = load_member_from_setting(
        'RAPID_PROTOTYPING_SPRINTS_MODULE')

    all_tasks = []
    # TODO The onerror parameter is basically a workaround to ignore errors
    # The reason for that being, that in my case, the GeoDjango package was in
    # the path, permanently requesting certain libraries on import. Since they
    # were not present, the search was aborted with an OSError.
    for importer, package_name, _ in pkgutil.walk_packages(
            onerror=lambda p: p):
        if not package_name.endswith('_costs'):
            continue
        if not getattr(settings, 'TEST_RUN', None) and (
                '.test_app.' in package_name):  # pragma: nocover
            continue
        costs = load_member(package_name + '.costs')
        for task in costs:
            all_tasks.append(task)
    sorted_tasks = sorted(all_tasks, key=itemgetter('id'))

    for sprint in sprints:
        remaining_time = 0
        sprint['tasks'] = []
        for task in sorted_tasks:
            if task.get('sprint') == sprint.get('id'):
                if not task.get('actual_time'):
                    remaining_time += \
                        task.get('developer_time') or task.get('time')
                sprint.get('tasks').append(task)
        sprint['remaining_time'] = remaining_time
        sprint['remaining_hours'] = round(float(remaining_time) / 60, 2)
    return sprints


def get_counter(counter):
    """
    Increases the counter by 1 and returns the changed list.

    This is a little hack. It works because lists are mutable. So in your
    ``context/home_costs.py`` you would something like this::

        from rapid_prototyping.context.utils import get_counter
        MAIN_ID = 100
        counter = [-1]
        costs = {
            'id': MAIN_ID + get_counter(counter)[0],
            ...
        }

    :param counter: A list which has one item, which is an integer, i.e.
      ``[-1]``.

    """
    counter[0] = counter[0] + 1
    return counter


def append_overhead_costs(costs, new_id, overhead_percentage=0.15):
    """
    Adds 15% overhead costs to the list of costs.

    Usage::

        from rapid_prototyping.context.utils import append_overhead_costs
        costs = [
            ....
        ]
        costs = append_overhead_costs(costs, MAIN_ID + get_counter(counter)[0])

    :param costs: Your final list of costs.
    :param new_id: The id that this new item should get.

    """
    total_time = 0
    for item in costs:
        total_time += item['time']

    costs.append({
        'id': new_id,
        'task': 'Overhead, Bufixes & Iterations',
        'time': total_time * overhead_percentage, },
    )
    return costs

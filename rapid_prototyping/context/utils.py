"""Utilify functions that are useful for template context modules."""
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

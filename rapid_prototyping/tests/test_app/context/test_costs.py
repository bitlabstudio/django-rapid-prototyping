from rapid_prototyping.context.utils import append_overhead_costs, get_counter


MAIN_ID = 100
counter = [-1]

costs = [
    {
        'id': MAIN_ID + get_counter(counter)[0],
        'task': 'First task',
        'time': 90,
        'developer_time': 110,
        'link': 'http://www.google.com',
        'sprint': 1,
    },
    {
        'id': MAIN_ID + get_counter(counter)[0],
        'task': 'Second task',
        'time': 60,
    },
]

costs = append_overhead_costs(costs, MAIN_ID + get_counter(counter)[0])

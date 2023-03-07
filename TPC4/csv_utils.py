import re
from functools import reduce

table = {
    'media': lambda l: sum(l) / len(l),
    'sum': lambda l: sum(l),
    'maximum': lambda l: reduce(lambda x, y: x if x > y else y, l),
    'minimum': lambda l: reduce(lambda x, y: x if x < y else y, l)
}

def range_maker(line: str, range) -> list[str]:
    ...

def make_match(header: str):
    for field in re.findall(re.compile(r'\w,?'), header):
        if field != '':
            field_matcher = re.compile(r'(?P<field>\w.*)({(?P<range>\d+(-\d+)?)})?(::(?P<function>media|sum|maximum|minimum))?')
            field_dispatcher = re.match(field_matcher, field).groupdict()

            if field_dispatcher['range'] != '':
                span = [int(x) for x in field_dispatcher['range'].split(',')]
                field_dispatcher['range'] = range(span[0], range[0]+1) if len(span) == 1 else range(span[0], span[-1])


            if field_dispatcher['function'] != '':
                field_dispatcher['function'] = table[field_dispatcher['function']]
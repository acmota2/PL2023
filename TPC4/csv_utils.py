import re
from functools import reduce

table = {
    'media': lambda l: sum(l) / len(l),
    'sum': lambda l: sum(l),
    'maximum': lambda l: reduce(lambda x, y: x if x > y else y, l),
    'minimum': lambda l: reduce(lambda x, y: x if x < y else y, l),
    '': None
}

def make_match(header: str) -> str:
    regex = r''
    for field in re.findall(re.compile(r'\w,?'), header):
        if field != '':
            field_matcher = re.compile(r'(?P<field>\w.*)({(?P<range>\d+(-\d+)?)})?(::(?P<function>media|sum|maximum|minimum))?')
            field_dispatcher = re.match(field_matcher, field).groupdict()

            if field_dispatcher['range'] != '':
                span = [int(x) for x in field_dispatcher['range'].split(',')]
                regex += (fr'(?P<{field}>(.*,?){{{span[0]}}})' if len(span) == 1 else fr'(?P<{field}>(.*,?){{{span[0]}-{span[-1]}}})')
            else:
                regex += fr'(?P<{field}>.*)'
    
    return regex
            
            # if f := field_dispatcher['function'] != '':
            #     regex += fr'(?P<{field}_{f}>.*)'